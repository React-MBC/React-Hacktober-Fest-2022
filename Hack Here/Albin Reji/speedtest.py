# pip install pyspeedtest
# pip install speedtest
# pip install speedtest-cli#method 1
import speedtestspeedTest = speedtest.Speedtest() 
print(speedTest.get_best_server())#Check download speed 
print(speedTest.download())#Check upload speed
print(speedTest.upload())# Method 2import pyspeedtest
st = pyspeedtest.SpeedTest()
st.ping()
st.download()
st.upload()