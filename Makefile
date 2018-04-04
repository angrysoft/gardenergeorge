path = static/scripts

all: main index lawncare maintenance freequote css

main: $(path)/main.dart
	dart2js -m -o $(path)/main.dart.js $(path)/main.dart

index: $(path)/index.dart
	dart2js -m -o $(path)/index.dart.js $(path)/index.dart

lawncare: $(path)/lawncare.dart
	dart2js -m -o $(path)/lawncare.dart.js $(path)/lawncare.dart

maintenance: $(path)/maintenance.dart
	dart2js -m -o $(path)/maintenance.dart.js $(path)/maintenance.dart

freequote: $(path)/freequote.dart
	dart2js -m -o $(path)/freequote.dart.js $(path)/freequote.dart

css: $(path)/styles.css
	sassc -t compressed $(path)/styles.css $(path)/styles.min.css
