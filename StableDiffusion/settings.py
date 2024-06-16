negative_prompt = "blurry, dark, low resolution, overexposed, underexposed, poorly lit, grainy, distorted, incorrect colors, unnatural, unrealistic, out of focus, chaotic composition, unattractive, unappealing, dull, lifeless, messy, noisy"
num_inference_steps = 25
height = 624
width = 624
dataset_path = "dataset.xlsx"
pathSD = "StableDiffusion/models/realisticVisionV60B1_v51HyperVAE.safetensors"
background_path = "banners/"
short_product_name = { "Потребительский кредит": "ПК",
                       "Автомобильный кредит": "АВ",
                       "Кредит под залог недвижимости": "КПЗН",
                        "Кредитная карта": " КК",
                       "Премиальная дебетовая карта": "Премиум",
                       "Ипотека": "Ипотека"},