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

# Pokretanje
Izabrani model spremljen je u 
