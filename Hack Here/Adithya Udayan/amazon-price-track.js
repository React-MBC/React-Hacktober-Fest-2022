const rp = require('request-promise');
const cheerio = require('cheerio');
const dotenv = require('dotenv').config();
const express = require('express');
const nodemailer = require('nodemailer');
const CronJob = require("cron").CronJob;
const app = express();


let currentPrice = 0;
const PROD_URL = "https://www.amazon.in/Tide-Extra-Detergent-Washing-Powder/dp/B07ZQDFG9R?ref_=Oct_DLandingS_D_1713f719_60&smid=AT95IG9ONZD7S&th=1";
let newPrice = 0;

const job = new CronJob('*/5 * * * *', function() {
    console.log("running");
    getPrice().then((newPrice,rej)=>{
        if(rej){
            getPrice();
        }
        if(currentPrice == 0){
            currentPrice = newPrice
        }
        if(currentPrice != newPrice){
            main()
            console.log(newPrice);
    }
        
    })
}, true);

job.start();

function getPrice(){
    return new Promise((resolve , rejects)=>{
        
        rp(PROD_URL).then((res)=>{
            const $ = cheerio.load(res);
            newPrice =    $('.apexPriceToPay > span:nth-child(1)').text().substring(1) ||  $('#corePrice_feature_div > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)').text().substring(1) || $('#corePrice_feature_div > div:nth-child(1) > span:nth-child(2) > span:nth-child(2) > span:nth-child(2)').text().slice(0,-1);
            newPrice = parseFloat(newPrice.replace(/,/g, ''))
            if(newPrice != undefined){
                
                resolve(newPrice);
            }
            rejects("Data unavailable")
            
        })
    }
    )
}

async function main() {
  
    let transporter = nodemailer.createTransport({
        service : "Gmail", // true for 465, false for other ports
      auth: {
        user : process.env.USER_MAIL, 
        pass : process.env.PASS,
      },
    });
  
    // send mail with defined transport object
    let info = await transporter.sendMail({
      from: '"Amazon price tracker" ourMail@gmail.com', // sender address
      to: process.env.TO_MAIL , // list of receivers
      subject: "Amazon price tracker", // Subject line
      text: ``, // plain text body
      html: `<b>The price of item ${PROD_URL} has dropped to ${newPrice}.</b>`, // html body
    });
  
    console.log("Message sent: %s", info.messageId);
  
  }

app.listen(3000)
