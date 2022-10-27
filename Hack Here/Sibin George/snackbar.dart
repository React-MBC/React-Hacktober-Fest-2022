import 'package:flutter/material.dart';
import 'package:another_flushbar/flushbar.dart';
import 'package:another_flushbar/flushbar_helper.dart';

void main() {
runApp(const MyApp());
}

class MyApp extends StatelessWidget {
const MyApp({Key? key}) : super(key: key);
@override
Widget build(BuildContext context) {
	return MaterialApp(
	debugShowCheckedModeBanner: false,
	title: 'Flutter Flushbar Tutorial',
	theme: ThemeData(
		primarySwatch: Colors.green,
	),
	home: MyHomePage(),
	);
}
}

class MyHomePage extends StatefulWidget {
@override
State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
@override
Widget build(BuildContext context) {
	return Scaffold(
	appBar: AppBar(title: Text("GeeksForGeeks"), centerTitle: true),
	body: Center(
		child: Column(
		children: [
			SizedBox(
			height: 40,
			),
			ElevatedButton(
				onPressed: () {
					
				// invoking show_Simple_Snackbar function
				show_Simple_Snackbar(context);
				},
				child: Text("Simple Snackbar with Flushbar")),
			ElevatedButton(
				onPressed: () {
					
				// calling function to show flushbar with icon
				show_Icon_Flushbar(context);
				},
				child: Text("Flushbar with Icon")),
			ElevatedButton(
				onPressed: () {
				//calling show Customized Flushbar
				show_Custom_Flushbar(context);
				},
				child: Text("Flushbar with gradient colors")),
			ElevatedButton(
				onPressed: () {
					
				// calling function to FlushbarHelper
				show_FlushbarHelper(context);
				},
				child: Text("Flushbar Helper")),
			ElevatedButton(
				onPressed: () {
					
				// calling function to show flushbar with button
				show_Button_Flushbar(context);
				},
				child: Text("Flushbar with Button"))
		],
		),
	),
	);
}

void show_Simple_Snackbar(BuildContext context) {
	Flushbar(
	duration: Duration(seconds: 3),
	title: "This is simple flushbar",
	message: "Hey, you are a registered user now.",
	)..show(context);
}

void show_Icon_Flushbar(BuildContext context) {
	Flushbar(
	icon: Icon(
		Icons.email_outlined,
		color: Colors.white,
		size: 30,
	),
	backgroundColor: Color(0xFF0277BD),
	duration: Duration(seconds: 4),
	message: "This email is already registered.",
	messageSize: 18,
	titleText: Text("Flushbar with Icon.",
		style: TextStyle(
			fontSize: 16,
			fontWeight: FontWeight.bold,
			color: Colors.white)),
	)..show(context);
}

void show_Custom_Flushbar(BuildContext context) {
	Flushbar(
	duration: Duration(seconds: 3),
	margin: EdgeInsets.all(8),
	padding: EdgeInsets.all(10),

	backgroundGradient: LinearGradient(
		colors: [
		Colors.pink.shade500,
		Colors.pink.shade300,
		Colors.pink.shade100
		],
		stops: [0.4, 0.7, 1],
	),
	boxShadows: [
		BoxShadow(
		color: Colors.black45,
		offset: Offset(3, 3),
		blurRadius: 3,
		),
	],
		
	// All of the previous Flushbars could be dismissed
	// by swiping to any direction
	dismissDirection: FlushbarDismissDirection.HORIZONTAL,
		
	// The default curve is Curves.easeOut
	forwardAnimationCurve: Curves.fastLinearToSlowEaseIn,
	title: 'This is a floating Flushbar',
	message: 'Welcome to Flutter community.',
	messageSize: 17,
	)..show(context);
}

void show_FlushbarHelper(BuildContext context) {
	FlushbarHelper.createInformation(
		title: "Flushbar Helper", message: "This is illegal action.")
	..show(context);
}

void show_Button_Flushbar(BuildContext context) {
	Flushbar(
	mainButton: ButtonBar(
		children: [
		GestureDetector(
			onTap: () {
			print("You clicked me!");
			},
			child: Text(
			"Click me",
			style: TextStyle(color: Colors.white),
			),
		)
		],
	),
	backgroundColor: Colors.black,
	title: "Flushbar with Button",
	message: "We require additional information.",
	messageSize: 17,
	duration: Duration(seconds: 4),
	)..show(context);
}
}
