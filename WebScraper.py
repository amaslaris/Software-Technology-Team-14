from bs4 import BeautifulSoup
import requests

html_text1 = requests.get('https://www.skywalker.gr/el/aggelies-ergasias?offset=100&page=1').text #πρώτη ιστοσελίδα για scraping
soup1 = BeautifulSoup(html_text1, 'lxml')
jobs1 = soup1.find_all('li', class_ = 'res') #πρόσβαση στις πρώτες 100 αγγελίες της πρώτης ιστοσελίδας

for job in jobs1: #πρόσβαση σε κάθε μια αγγελία της πρώτης ιστοσελίδας ξεχωριστά

    title = job.find('span', class_ = 'listing-title').text #εξαγωγή θέσης εργασίας
    location = job.find('div', class_ = 'states-list mb-2').text #εξαγωγή τοποθεσίας
    info = job.find('a', class_ = 'previewJob')['href'] #εξαγωγή link
        
    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
    print(f"Πληροφορίες: {info}") #εκτύπωση link
    print('')

html_text2 = requests.get('https://www.kariera.gr/jobs?page=0&limit=100').text #δεύτερη ιστοσελίδα για scraping
soup2 = BeautifulSoup(html_text2, 'lxml')
jobs2 = soup2.find_all('section', class_ = 'JobCard_compWrap__915q5') #πρόσβαση στις πρώτες 100 αγγελίες της δεύτερης ιστοσελίδας

for job in jobs2: #πρόσβαση σε κάθε μια αγγελία της δεύτερης ιστοσελίδας ξεχωριστά

    title = job.find('a', class_ = 'h4 JobCard_text__2DNt5').text #εξαγωγή θέσης εργασίας
    location = job.find('span', class_ = 'small-body-text').text #εξαγωγή τοποθεσίας
    info = 'https://www.kariera.gr' + job.find('a', class_ = 'h4 JobCard_text__2DNt5')['href'] #εξαγωγή link
        
    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
    print(f"Πληροφορίες: {info}") #εκτύπωση link
    print('')

html_text3 = requests.get('https://www.randstad.gr/theseis-ergasias/').text #τρίτη ιστοσελίδα για scraping
soup3 = BeautifulSoup(html_text3, 'lxml')
jobs3 = soup3.find_all('li', class_ = 'cards__item bg-variant-white') #πρόσβαση στις πρώτες 30 αγγελίες της τρίτης ιστοσελίδας

for job in jobs3: #πρόσβαση σε κάθε μια αγγελία της τρίτης ιστοσελίδας ξεχωριστά

    title = job.find('a', class_ = 'cards__link').text #εξαγωγή θέσης εργασίας
    location = job.find('li', class_ = 'cards__meta-item').text #εξαγωγή τοποθεσίας
    info = 'https://www.randstad.gr' + job.find('a', class_ = 'cards__link')['href'] #εξαγωγή link
        
    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
    print(f"Πληροφορίες: {info}") #εκτύπωση link
    print('')


print('Διαθέσιμα Φίλτρα:\n 1.Θέση εργασίας\n 2.Τοποθεσία\nΘα ήθελες να φιλτράρεις τα αποτελέσματα; (Y/N)')
answer = input('>')

if answer=='Y' or answer=='y':
    print('Εισήγαγε τον αριθμό του φίλτρου:')
    filter = int(input('>'))

    match filter:
        case 1:
            print('Θέση εργασίας:')
            job_title = input('>')
            
            for job in jobs1:
                title = job.find('span', class_ = 'listing-title').text #εξαγωγή θέσης εργασίας
                location = job.find('div', class_ = 'states-list mb-2').text #εξαγωγή τοποθεσίας
                info = job.find('a', class_ = 'previewJob')['href'] #εξαγωγή link

                if job_title in title: #εκτύπωση αποτελεσμάτων βάση φιλτραρίσματος
                    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
                    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
                    print(f"Πληροφορίες: {info}") #εκτύπωση link
                    print('')

            for job in jobs2: #πρόσβαση σε κάθε μια αγγελία της πρώτης ιστοσελίδας ξεχωριστά
                title = job.find('a', class_ = 'h4 JobCard_text__2DNt5').text #εξαγωγή θέσης εργασίας
                location = job.find('span', class_ = 'small-body-text').text #εξαγωγή τοποθεσίας
                info = 'https://www.kariera.gr' + job.find('a', class_ = 'h4 JobCard_text__2DNt5')['href'] #εξαγωγή link

                if job_title in title: #εκτύπωση αποτελεσμάτων βάση φιλτραρίσματος
                    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
                    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
                    print(f"Πληροφορίες: {info}") #εκτύπωση link
                    print('')

            for job in jobs3: #πρόσβαση σε κάθε μια αγγελία της τρίτης ιστοσελίδας ξεχωριστά
                title = job.find('a', class_ = 'cards__link').text #εξαγωγή θέσης εργασίας
                location = job.find('li', class_ = 'cards__meta-item').text #εξαγωγή τοποθεσίας
                info = 'https://www.randstad.gr' + job.find('a', class_ = 'cards__link')['href'] #εξαγωγή link
        
                if job_title in title: #εκτύπωση αποτελεσμάτων βάση φιλτραρίσματος
                    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
                    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
                    print(f"Πληροφορίες: {info}") #εκτύπωση link
                    print('')        

        case 2:
            print('Τοποθεσία:')
            job_location = input('>')
            
            for job in jobs1:
                title = job.find('span', class_ = 'listing-title').text #εξαγωγή θέσης εργασίας
                location = job.find('div', class_ = 'states-list mb-2').text #εξαγωγή τοποθεσίας
                info = job.find('a', class_ = 'previewJob')['href'] #εξαγωγή link

                if job_location in location: #εκτύπωση αποτελεσμάτων βάση φιλτραρίσματος
                    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
                    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
                    print(f"Πληροφορίες: {info}") #εκτύπωση link
                    print('')

            for job in jobs2: #πρόσβαση σε κάθε μια αγγελία της πρώτης ιστοσελίδας ξεχωριστά
                title = job.find('a', class_ = 'h4 JobCard_text__2DNt5').text #εξαγωγή θέσης εργασίας
                location = job.find('span', class_ = 'small-body-text').text #εξαγωγή τοποθεσίας
                info = 'https://www.kariera.gr' + job.find('a', class_ = 'h4 JobCard_text__2DNt5')['href'] #εξαγωγή link

                if job_location in location: #εκτύπωση αποτελεσμάτων βάση φιλτραρίσματος
                    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
                    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
                    print(f"Πληροφορίες: {info}") #εκτύπωση link
                    print('')

            for job in jobs3: #πρόσβαση σε κάθε μια αγγελία της τρίτης ιστοσελίδας ξεχωριστά
                title = job.find('a', class_ = 'cards__link').text #εξαγωγή θέσης εργασίας
                location = job.find('li', class_ = 'cards__meta-item').text #εξαγωγή τοποθεσίας
                info = 'https://www.randstad.gr' + job.find('a', class_ = 'cards__link')['href'] #εξαγωγή link
        
                if job_location in location: #εκτύπωση αποτελεσμάτων βάση φιλτραρίσματος
                    print(f"Θέση Εργασίας: {title.strip()}") #εκτύπωση θέσης εργασίας
                    print(f"Τοποθεσία: {location.strip()}") #εκτύπωση τοποθεσίας
                    print(f"Πληροφορίες: {info}") #εκτύπωση link
                    print('')                 
                           
        case _:
            print('Δεν υπάρχει διαθέσιμο φίλτρο')
