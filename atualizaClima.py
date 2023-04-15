import requests


# Configuraçã API
class Atualizaclima:

  def atu_clima(cidade):
    API_KEY = "c8bdb8342634bf01667eff378872945d"
    vLink = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    req = requests.get(vLink)

    req_dic = req.json()

    status = req_dic["cod"]

    if status == 200:
      desc = req_dic['weather'][0]['description']
      temperatura = round(req_dic['main']['temp'] - 273.15)
      cidade_api = req_dic["name"]
      result = (
        f"🏙 **{cidade_api}** \n 🌥 {desc} \n 🌡 {temperatura}Cº"
      )
    else:
      result = (f"Não foi possível encontrar cidade com: {cidade}")

    return (result)
