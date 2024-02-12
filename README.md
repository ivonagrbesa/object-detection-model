# Model za detekciju objekata
Razvijen je AI model za detekciju i lociranje ovaca i sova na slikama. Dobiveni model nastao je dotreniranjem prethodno treniranog YOLOv8n.pt modela. 
## Skup podataka
Korišten je skup slika OpenImagesv7, iz kojeg je pomoću FiftyOne preuzet manji broj slika ovaca i sova, zajedno s labelama za detekciju i klasifikaciju. Skup za treniranje sadrži 70 slika, a skup za validaciju i skup za treniranje svaki po 15 slika. Anotacije OpenImages slika transformirane su u format prikladan za korišten YOLO modela i kreirana je config.yaml datoteka.
## Treniranje modela i rezultati
Dobiveni model nastao je dotreniranjem modela YOLOv8n.pt, pri čemu su korišteni hiperparametri: batch size 16 i 32, 10 epoha, patience 2, learning rate 0.01. Ovako razvijeni model pri validaciji postiže ukupnu preciznost mAP50 od 82%, mAP50-95 64%, box precision 66% i recall 85%. 
![Treniranje modela](https://github.com/ivonagrbesa/object-detection-model/blob/main/results.png)

Model uspješno detektira većinu traženih objekata na slici i sigurnost (confidence) ima uglavnom visoke vrijednosti. 
![Detekcija objekata](https://github.com/ivonagrbesa/object-detection-model/blob/main/results.jpg)

Provedeno je i treniranje YOLOv8s.pt modela, kojim su dobiveni slični rezultati, ali s većom pristranošću između klasa (u korist klase sova) i lošijom izvedbom na skupu za testiranje pa je prvotni model izabran kao finalni.

# Upute za pokretanje modela
Izabrani model spremljen je u (https://github.com/ivonagrbesa/object-detection-model/blob/main/runs/detect/train20/weights/best.pt), a pokreće se unutar datoteke detection.py. Potrebno je postaviti da datoteka detection.py bude u istom direktoriju kao datoteka DetectObjects.py te sve putanje prilagoditi direktorijima računala na kojem se pokreće. Funkcija Detect kao ulazni parametar prima niz putanja za jednu ili više slika iz skupa za testiranje. Funkcija Detect učitava model, provodi interferenciju te ispisuje koliko je i kojih objekata detektirano, otvara se unesena slika s uokvirenim detektiranim objektima i pouzdanošću.

```
from DetectObjects import *

p = ['C:/Users/Ivona/Desktop/Codeasy/yolo_test_dataset/10abae5a94fe5368.jpg']
Detect(p)
```
Output dobiven pokretanjem modela prikazan je u nastavku.
![Output pokretanja modela](https://github.com/ivonagrbesa/object-detection-model/blob/main/DetectionOutput.PNG)
