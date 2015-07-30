#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Panagiotis
# @Date:   2015-07-30 17:28:21
# @Last Modified by:   Panagiotis
# @Last Modified time: 2015-07-30 18:17:55

TransmissionType = {
		'Automatic': [u'Ημιαυτόματο κιβώτιο', u'Αυτόματη μετάδοση', u'Αυτόματο σειριακό κιβώτιο', u'Αυτόματο συνεχούς μεταβαλόμενηςσχ./σεριακό κιβώτιο',u'Αυτόματο συνεχούς μεταβαλόμενης σχ. Κιβώτιο'],
		'Manual': [u'Χειροκίνητο κιβωτίο με ομάδες επιλογών', u'Χειροκίνητο κιβώτιο', u'Χειροκίνητο σειριακό κιβώτιο']
}

BodyType = {
	'4x4': [u'4Χ4 Σοφτ-τοπ',u'4Χ4 Χάρντ-τοπ'],
	'Cabriolet': [u'Ρόαντστερ',u'Κάμπριο',u'Τάργκα'],
	u'Coupé': [u'Κουπέ'],
	'Estate': [u'Στέ\'ι\'σον Βάγκον',u'Στέϊσον Βάγκον',u'Στέ´ι´σον Βάγκον'],
	'Hatchback': [u'Χάτσμπακ'],
	'MPV': [u'Πολυμορφικά οχημ.(MPV)'],
	'Saloon': [u'Λιμουζίνα',u'Σεντάν']
}

BreaksType = {
	'(Not specified)': ['no link'],
	'Disk': [u'Δισκόφρενα Αεριζόμενα', u'Δισκόφρενα', u'Διπλά Δισκόφρενα'],
	'Drum': [u'Ταμπουρόφρενα']
}




	# df['EUEmissionsTierConformance'] = df['EUEmissionsTierConformance'].str.replace('no link','(Not specified)')
	# df['EUEmissionsTierConformance'] = df['EUEmissionsTierConformance'].str.replace(u'Νόρμα εκπομπών EEV','EEV')
	# df['EUEmissionsTierConformance'] = df['EUEmissionsTierConformance'].str.replace(u'Νόρμα καταλυτών Euro2','Euro 2')
	# df['EUEmissionsTierConformance'] = df['EUEmissionsTierConformance'].str.replace(u'Νόρμα εκπομπών Euro3','Euro 3')
	# df['EUEmissionsTierConformance'] = df['EUEmissionsTierConformance'].str.replace(u'Νόρμα εκπομπών Euro4','Euro 4')
	# df['EUEmissionsTierConformance'] = df['EUEmissionsTierConformance'].str.replace(u'Νόρμα εκπομπών Euro5','Euro 5')
	# df['EUEmissionsTierConformance'] = df['EUEmissionsTierConformance'].str.replace(u'Νόρμα εκπομπών Euro6','Euro 6')

	# df['FuelInjection'] = df['FuelInjection'].str.replace('no link','(Not specified)')
	# df['FuelInjection'] = df['FuelInjection'].str.replace(u'Συμπιεστής Roots','Roots Compressor')
	# df['FuelInjection'] = df['FuelInjection'].str.replace(u'Tούρμπο','Turbo')
	# df['FuelInjection'] = df['FuelInjection'].str.replace(u'Τούρμπο μεταβλητής γεωμετρίας','Variable-geometry turbochargers')
	
	# df['FuelType'] = df['FuelType'].str.replace(u'Πετρέλαιο','Diesel')
	# df['FuelType'] = df['FuelType'].str.replace(u'Ηλεκτρισμός (Μπαταρία)','Electricity')
	# df['FuelType'] = df['FuelType'].str.replace(u'Πετρέλαιο & ηλεκτρισμός','Electricity and Diesel')
	# df['FuelType'] = df['FuelType'].str.replace(u'Βενζίνη αμόλυβδη και Ηλεκτρισμός','Electricity and Petrol')
	# df['FuelType'] = df['FuelType'].str.replace(u'Βενζίνη ή Αέριο','LPG')
	# df['FuelType'] = df['FuelType'].str.replace(u'Αέριο','LPG')
	# df['FuelType'] = df['FuelType'].str.replace(u'Βενζίνη με μόλυβδο','Petrol')
	# df['FuelType'] = df['FuelType'].str.replace(u'Βενζίνη αμόλυβδη','Petrol')

	# df['Manufacturer'] = df['Manufacturer'].str.replace('ABARTH','Abarth')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('ALFA ROMEO','Alfa Romeo')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('ASTON MARTIN','Aston Martin')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('AUDI','Audi')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('BMW','BMW')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('CADILLAC','Cadillac')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('CHANGAN','Changan')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('CHEVROLET','Chevrolet')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('CHRYSLER','Chrysler')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('CITROEN',u'Citroën')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('DACIA','Dacia')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('DAEWOO','Daewoo')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('DAEWOO - FSO','Daewoo')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('DAIHATSU','Daihatsu')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('DFM','DFM')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('DODGE','Dodge')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('FIAT','Fiat')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('FORD','Ford')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('FORD USA','Ford')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('HONDA','Honda')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('HX AUTO','Hx Auto')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('HYUNDAI','Hyundai')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('INFINITI','Infiniti')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('ISUZU','Isuzu')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('JAC','Jac')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('JEEP','Jeep')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('KIA','KIA')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('LADA','Lada')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('LANCIA','Lancia')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('LAND ROVER','Land Rover')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('LANDWIND','Landwind')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('LEXUS','Lexus')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('LIFAN','Lifan')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('MAZDA','Mazda')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('MERCEDES-BENZ','Mercedes-Benz')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('MG','MG')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('MINI','Mini')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('MITSUBISHI','Mitsubishi')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('NISSAN','Nissan')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('OPEL','Opel')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('PEUGEOT','Peugeot')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('PIAGGIO','Piaggio')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('RENAULT','Renault')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('ROVER','Rover')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SAAB','Saab')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SEAT','Seat')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SH AUTO','Sh Auto')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SKODA','Skoda')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SMART','Smart')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SSANGYONG','Ssangyong')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SUBARU','Subaru')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('SUZUKI','Suzuki')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('TATA','Tata')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('TOYOTA','Toyota')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('VOLKSWAGEN','Volkswagen')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('VOLVO','Volvo')
	# df['Manufacturer'] = df['Manufacturer'].str.replace('ZASTAVA','Zastava')

	# df['NumberOfDoors'] = df['NumberOfDoors'].str.replace('2','2 or 3')
	# df['NumberOfDoors'] = df['NumberOfDoors'].str.replace('3','2 or 3')
	# df['NumberOfDoors'] = df['NumberOfDoors'].str.replace('4','4 or 5')
	# df['NumberOfDoors'] = df['NumberOfDoors'].str.replace('5','4 or 5')

	# df['Segmentation'] = df['Segmentation'].str.replace('Μεγάλα','Large')
	# df['Segmentation'] = df['Segmentation'].str.replace('Πολυτελείας','Luxury')
	# df['Segmentation'] = df['Segmentation'].str.replace('Μεσαία','Medium')
	# df['Segmentation'] = df['Segmentation'].str.replace('Μίκρο','Micro')
	# df['Segmentation'] = df['Segmentation'].str.replace('Μίνι','Mini')
	# df['Segmentation'] = df['Segmentation'].str.replace('Εκτός δρόμου','Off Road')
	# df['Segmentation'] = df['Segmentation'].str.replace('Μικρά','Small')
	# df['Segmentation'] = df['Segmentation'].str.replace('Μικρομεσαία','Small/Medium')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Αυτόματη μετάδοση','Automatic')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Αυτόματο σειριακό κιβώτιο','Automatic')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Αυτόματο συνεχούς μεταβαλόμενης σχ. Κιβώτιο','Automatic')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Αυτόματο συνεχούς μεταβαλόμενηςσχ./σεριακό κιβώτιο','Automatic')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Ημιαυτόματο κιβώτιο','Automatic')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Χειροκίνητο κιβωτίο με ομάδες επιλογών','Manual')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Χειροκίνητο κιβώτιο','Manual')
	# df['TransmissionType'] = df['TransmissionType'].str.replace(u'Χειροκίνητο σειριακό κιβώτιο','Manual')

	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Τετρακίνηση μόνιμη','4-Wheel Drive')
	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Tετρακίνηση επιλ.εκτός δρόμου','4-Wheel Drive')
	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Τετρακίνηση','4-Wheel Drive')
	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Τετρακίνηση επιλεγόμενη','4-Wheel Drive')
	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Τετρακίνηση με ικαν.εκτός δρόμ','4-Wheel Drive')
	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Τετρακίνηση μόν.εκτός δρόμου','4-Wheel Drive')
	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Εμπρός','Front Wheel Drive')
	# df['WheelDrive'] = df['WheelDrive'].str.replace(u'Πίσω','Rear Wheel Drive')
