#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Panagiotis
# @Date:   2015-07-30 17:28:21
# @Last Modified by:   Panagiotis
# @Last Modified time: 2015-07-31 12:33:21

BodyType = {
	'4x4': ['4Χ4 Σοφτ-τοπ', '4Χ4 Χάρντ-τοπ'],
	'Cabriolet': ['Ρόαντστερ', 'Κάμπριο', 'Τάργκα'],
	'Coupé': ['Κουπέ'],
	'Estate': ['Στέ\'ι\'σον Βάγκον', 'Στέϊσον Βάγκον', 'Στέ´ι´σον Βάγκον'],
	'Hatchback': ['Χάτσμπακ'],
	'MPV': ['Πολυμορφικά οχημ.(MPV)'],
	'Saloon': ['Λιμουζίνα', 'Σεντάν'],
	'UNSUPPORTED': ['Ημιφορτηγό Κόμπι', 'Λεωφορειάκι', 'Κλειστό Φορτηγό/Καμπίνα', 'Ημιφορτηγό Βαν', 'Ημιφ./Φορτ. Πλαίσιο', 'Ημιφ. Πλαίσιο/Καμπίνα', 'Ημιφ. Πλαίσιο/2πλης Καμπ.', 'Ημιφ. Πικ-απ Χαμηλωμένο', 'Ημιφ. Κόμπι/2πλης Καμπ.', 'Επιβατικό-Βαν', 'Επιβ.-Βαν/2πλης Καμπ.', 'Επιβ.-Βαν με Παράθυρα', 'Εμπροσθοκάμπινο φορτηγό σταθερής καρότσας', 'Ημιφ. Πικ-απ']
}

BreaksType = {
	'(Not specified)': ['no link'],
	'Disk': ['Δισκόφρενα Αεριζόμενα', 'Δισκόφρενα', 'Διπλά Δισκόφρενα'],
	'Drum': ['Ταμπουρόφρενα']
}

EUEmissionsTierConformance = {
	'(Not specified)': ['no link'],
	'EEV': ['Νόρμα εκπομπών EEV'],
	'Euro 2': ['Νόρμα καταλυτών Euro2'],
	'Euro 3': ['Νόρμα εκπομπών Euro3'],
	'Euro 4': ['Νόρμα εκπομπών Euro4'],
	'Euro 5': ['Νόρμα εκπομπών Euro5'],
	'Euro 6': ['Νόρμα εκπομπών Euro6'],
	'UNSUPPORTED': ['Νόρμα καταλυτών Euro1']
}

FuelInjection = {
	'(Not specified)': ['no link'],
	
	'Turbo': ['Tούρμπο'],
	'Compressor and Turbo': ['Compressor and Turbo'],
	'Variable-geometry turbochargers': ['Τούρμπο μεταβλητής γεωμετρίας'],
	'Roots Compressor': ['Συμπιεστής Roots']
}
	
FuelType = {
	'Diesel': ['Πετρέλαιο'],
	'Electricity': ['Ηλεκτρισμός (Μπαταρία)'],
	'Electricity and Diesel': ['Πετρέλαιο & ηλεκτρισμός'],
	'Electricity and Petrol': ['Βενζίνη αμόλυβδη και Ηλεκτρισμός'],
	'LPG': ['Βενζίνη ή Αέριο', 'Αέριο'],
	'Petrol': ['Βενζίνη με μόλυβδο', 'Βενζίνη αμόλυβδη']
}
	
Manufacturer = {
	'Abarth': ['ABARTH'],
	'Alfa Romeo': ['ALFA ROMEO'],
	'Aston Martin': ['ASTON MARTIN'],
	'Audi': ['AUDI'],
	'BMW': ['BMW'],
	'Cadillac': ['CADILLAC'],
	'Changan': ['CHANGAN'],
	'Chevrolet': ['CHEVROLET'],
	'Chrysler': ['CHRYSLER'],
	'Citroën': ['CITROEN'],
	'Dacia': ['DACIA'],
	'Daewoo': ['DAEWOO', 'DAEWOO - FSO'],
	'Daihatsu': ['DAIHATSU'],
	'DFM': ['DFM'],
	'Dodge': ['DODGE'],
	'Fiat': ['FIAT'],
	'Ford': ['FORD', 'FORD USA'],
	'Honda': ['HONDA'],
	'Hx Auto': ['HX AUTO'],
	'Hyundai': ['HYUNDAI'],
	'Infiniti': ['INFINITI'],
	'Isuzu': ['ISUZU'],
	'Jac': ['JAC'],
	'Jeep': ['JEEP'],
	'KIA': ['KIA'],
	'Lada': ['LADA'],
	'Lancia': ['LANCIA'],
	'Land Rover': ['LAND ROVER'],
	'Landwind': ['LANDWIND'],
	'Lexus': ['LEXUS'],
	'Lifan': ['LIFAN'],
	'Mazda': ['MAZDA'],
	'Mercedes - Benz': ['MERCEDES - BENZ', 'MERCEDES-BENZ'],
	'MG': ['MG'],
	'Mini': ['MINI'],
	'Mitsubishi': ['MITSUBISHI'],
	'Nissan': ['NISSAN'],
	'Opel': ['OPEL'],
	'Peugeot': ['PEUGEOT'],
	'Piaggio': ['PIAGGIO'],
	'Renault': ['RENAULT'],
	'Rover': ['ROVER'],
	'Saab': ['SAAB'],
	'Seat': ['SEAT'],
	'Sh Auto': ['SH AUTO'],
	'Skoda': ['SKODA'],
	'Smart': ['SMART'],
	'Ssangyong': ['SSANGYONG'],
	'Subaru': ['SUBARU'],
	'Suzuki': ['SUZUKI'],
	'Tata': ['TATA'],
	'Toyota': ['TOYOTA'],
	'Volkswagen': ['VOLKSWAGEN'],
	'Volvo': ['VOLVO'],
	'Zastava': ['ZASTAVA'],
	'UNSUPPORTED': ['ASIA', 'BENTLEY', 'JAGUAR', 'HUMMER', 'FERRARI', 'LAMBORGHINI', 'LOTUS', 'MASERATI', 'PORSCHE', 'PONTIAC']
}

NumberOfDoors = {
	'2 or 3': ['2', '3'],
	'4 or 5': ['4', '5'],
}

Segmentation = {
	'Large': ['Μεγάλα'],
	'Luxury': ['Πολυτελείας'],
	'Medium': ['Μεσαία'],
	'Micro': ['Μίκρο'],
	'Mini': ['Μίνι'],
	'Off Road': ['Εκτός δρόμου'],
	'Small': ['Μικρά'],
	'Small / Medium': ['Μικρομεσαία'],
	'UNSUPPORTED': ['Μη συνδεόμενο(0003)', 'Ημιφορτηγό Βάν: θέσεων < 5', 'Ημιφορτηγό Βάν : θέσεων < 5', 'Μη συνδεόμενο (0003)']
}

TransmissionType = {
	'Automatic': ['Αυτόματη μετάδοση', 'Αυτόματο σειριακό κιβώτιο', 'Αυτόματο συνεχούς μεταβαλόμενης σχ. Κιβώτιο', 'Αυτόματο συνεχούς μεταβαλόμενηςσχ./σεριακό κιβώτιο', 'Ημιαυτόματο κιβώτιο'],
	'Manual': ['Χειροκίνητο κιβωτίο με ομάδες επιλογών', 'Χειροκίνητο κιβώτιο', 'Χειροκίνητο σειριακό κιβώτιο']
}

WheelDrive = {
	'4-Wheel Drive': ['Τετρακίνηση μόνιμη', 'Tετρακίνηση επιλ.εκτός δρόμου', 'Τετρακίνηση', 'Τετρακίνηση επιλεγόμενη', 'Τετρακίνηση με ικαν.εκτός δρόμ', 'Τετρακίνηση μόν.εκτός δρόμου'],
	'Front Wheel Drive': ['Εμπρός'],
	'Rear Wheel Drive': ['Πίσω']
}