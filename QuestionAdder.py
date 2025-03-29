from app import app,db
from models import Question

with app.app_context():

    questions = [ 
        Question(
            question="Etiketli (labelled) verilerle yapılan öğrenme işlemi hangi yapay zeka alt dalına aittir?",
            option_a="Sınıflandırma (Classification)",
            option_b="Kümeleme (Clustering)",
            option_c="Boyut indirgeme (Dimensionality Reduction)",
            option_d="Yeniden yapılandırma (Reconstruction)",
            correct_option="A"
        ),
        Question(
            question="Discord.py ile geliştirme yapmak için ihtiyacımız olan anahtara ne denir?",
            option_a="API Key",
            option_b="Secret Token",
            option_c="Bot Token",
            option_d="Access Key",
            correct_option="C"
        ),
        Question(question="Doğal Dil İşleme'nin temel amacı nedir?",
                option_a="Resim tanıma", option_b="Duyguları analiz etme", option_c="Diller arası çeviri", option_d="İnsan dilini bilgisayara anlatmak", correct_option="D"),

        Question(question="BeautifulSoup genellikle ne için kullanılır?",
                option_a="Veritabanı bağlantısı", option_b="Görüntü işleme", option_c="Web sayfası kazıma (scraping)", option_d="Oyun yapımı", correct_option="C"),
        Question(question="Yapay zeka modeli eğitildikten sonra hangi aşamaya geçilir?",
                option_a="Test ve Geliştirme", option_b="Analiz", option_c="Eğitim", option_d="Hazırlık", correct_option="A"),
        Question(question="Flask'ta bir sayfa rotası nasıl tanımlanır?",
                option_a="@route", option_b="@app.route", option_c="route()", option_d="def route()", correct_option="B"),
        Question(question="Discord.py ile mesajlara cevap vermek için hangi event kullanılır?",
                option_a="on_message", option_b="on_connect", option_c="on_ready", option_d="on_typing", correct_option="A"),
        Question(question="Flask'ta şablon dosyaları hangi klasörde bulunmalıdır?",
                option_a="static", option_b="templates", option_c="html", option_d="pages", correct_option="B"),
        Question(question="Yapay zeka ile görüntü tanıma genellikle hangi teknikle yapılır?",
                option_a="CNN", option_b="SVM", option_c="RNN", option_d="LSTM", correct_option="A"),
        Question(question="TensorFlow nedir?",
                option_a="Veritabanı", option_b="Yapay Zeka kütüphanesi", option_c="Web framework", option_d="Oyun motoru", correct_option="B"),]

    db.session.add_all(questions)
    db.session.commit()
    print("Sorular başarıyla eklendi")