import 'package:dark_theme_app/Button_tap_listener.dart';
import 'package:dark_theme_app/dark_theme_screen.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';


void main() {
runApp(MyApp());
}
class MyApp extends StatelessWidget {
	
// This widget is the root of your application.
@override
Widget build(BuildContext context) {
	return ChangeNotifierProvider<ButtonTapListenerClass>(
	create: (context) => ButtonTapListenerClass(),
	child: MaterialApp(
		debugShowCheckedModeBanner: false,
		title: 'Flutter Demo',
		
		// Themes
		darkTheme: ThemeData.dark(),
		home: DarkThemeExample(),
		theme: ThemeData(
			brightness: Brightness.dark,
			visualDensity: VisualDensity(horizontal: 2.0, vertical: 2.0),
			primaryColorLight: Color(0xff03203C),
			primaryColorDark: Color(0xff242B2E),
			
			// Icon Theme
			iconTheme:
				IconThemeData(color: Colors.amber, size: 15.0, opacity: 10),
			accentColor: Colors.amber,
			accentColorBrightness: Brightness.light),
	),
	);
}
}

