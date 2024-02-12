# Model za detekciju objekata
Razvijen je AI model za detekciju i lociranje ovaca i sova na slikama. Dobiveni model nastao je dotreniranjem prethodno treniranog YOLOv8n.pt modela. 
## Skup podataka
Korišten je skup slika OpenImagesv7, iz kojeg je pomoću FiftyOne preuzet manji broj slika ovaca i sova, zajedno s labelama za detekciju i klasifikaciju. Skup za treniranje sadrži 70 slika, a skup za validaciju i skup za treniranje svaki po 15 slika. Anotacije OpenImages slika transformirane su u format prikladan za korišten YOLO modela i kreirana je config.yaml datoteka.
## Treniranje modela
Dobiveni model nastao je dotreniranjem modela YOLOv8n.pt, pri čemu su korišteni hiperparametri: batch size 16 i 32, 10 epoha, Patience 2, learning rate 0.01. 
Validacijom se dobivaju sljedeći rezultati:
'''
Metrike na skupu za validaciju
mAP50-95:  0.641541208676182
mAP50:  0.8228177916443499
mAP75:  0.6612691845102405
'''
