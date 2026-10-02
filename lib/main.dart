import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    print("Building MyApp...");
    return MaterialApp(
      title: 'PS4 PKG Splitter',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('PS4 PKG Splitter'),
        ),
        body: const Center(
          child: Text('PS4 PKG Splitter is ready!'),
        ),
      ),
    );
  }
}
