
# ChatGPT AI Sohbet Botu

ChatGPT API'si geliştiricilere ve halka açıldı. Özellikle ChatGPT Plus'ın gücünü sağlayan "gpt-3.5-turbo" modeli 10 kat daha ucuz bir fiyata ve son derece hızlı bir şekilde piyasaya sunuldu. Temelde, OpenAI sonsuz olasılıkların kapısını açtı ve hatta bir kod yazılımcısı olmayan kişiler yeni ChatGPT API'sını uygulayarak kendi AI sohbet Botlarını oluşturabilirler. Bu makalede, ChatGPT API'sini kullanarak kendi AI sohbet botunu nasıl oluşturabileceğinizi öğreteceğiz. Ayrıca Gradio arabirimini de uyguladık, böylece AI modelini kolayca deneyebilir ve arkadaşlarınızla ve ailenizle paylaşabilirsiniz. Bu noktada, hadi kendi kişiselleştirilmiş AI'mizi ChatGPT API'si kullanarak nasıl oluşturacağımızı öğrenelim.


## Gereksinimler

- Python 3.x

## Kurulum

 1. Bu repo'yu klonlayın:
git clone https://github.com/https://github.com/barissglc/chatgpt-ai-bot.git


 2. Gereksinimleri yükleyin:

Başlamak için, bilgisayarınıza Python kurulu olması gerekmektedir. Python'un nasıl indirilip kurulacağına ilişkin aşağıdaki bağlantıyı kullanabilirsiniz:

https://www.python.org/downloads/

Ayrıca şu Python modüllerini de yüklemeniz gerekmektedir:

- `openai`
- `gradio`

Bu modülleri aşağıdaki komutu çalıştırarak yükleyebilirsiniz:

```
python -m pip install -U pip
pip install openai
pip install  gradio
```



 3. ChatGPT API anahtarınızı `app.py` dosyasındaki `openai.api_key` değişkenine atayın.

 4. Uygulamayı çalıştırın:

      Terminalinizi açıp(app.py konumunuzu bulup) python "C:\Users\barissglc\Desktop\app.py" yazın

5. Terminalinizden bağlantıları kopyalayın
    "http://127.0.0.1:7860/"
    ChatGPT API ile kendi AI sohbet robotunuzu bu şekilde oluşturabilirsiniz. ChatGPT destekli AI sohbet robotunuz yayında.
    Ayrıca herkese açık URL'yi kopyalayabilir ve arkadaşlarınız ve ailenizle paylaşabilirsiniz. Bağlantı 72 saat boyunca yayında olacak, ancak sunucu örneği bilgisayarınızda çalıştığı için bilgisayarınızı da açık tutmanız gerekiyor. 

## API Kullanımı

#### Buradan API Key olusturabilirsiniz.

https://platform.openai.com/account/api-keys

  
