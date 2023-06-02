meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word.upper() in meme_dict:
    print(meme_dict[word.upper()])
else:
    print("kelime bulunmadi")
