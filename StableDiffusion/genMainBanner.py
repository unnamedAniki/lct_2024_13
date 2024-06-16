from model import init_model, gen_logo
from settings import pathSD

prompts = {
    'Классический потребительский кредит': 'An image of a happy family in their living room, holding a document that represents a consumer loan approval. The background shows a cozy and modern home environment.',
    'Рефинансирование внутреннего ПК в Газпромбанке': 'An image of a person at a desk, reviewing loan documents with a Gazprombank logo in the background. The person looks relieved and happy.',
    'Рефинансирование внешнего ПК в другом банке': 'An image of a person shaking hands with a bank officer, with different bank logos in the background, representing external refinancing.',
    'Кредитная карта': 'An image of a shiny credit card with a futuristic design, being held by a smiling person. The background shows a shopping mall or an online shopping interface.',
    'Классический автокредит': 'An image of a happy couple standing next to a new car in a dealership. The car is modern and shiny, and the couple looks excited.',
    'Кредит под залог авто': 'An image of a person handing over car keys to a bank officer, with documents and a car in the background. The scene conveys trust and security.',
    'Ипотека': 'An image of a young family standing in front of a new house with a "Sold" sign. They look happy and excited about their new home.',
    'Рефинансирование ипотеки': 'An image of a person sitting at a desk, signing mortgage documents with a smiling bank officer. The background shows a modern bank interior.',
    'Кредит под залог недвижимости': 'An image of a person handing over house keys to a bank officer, with documents and a house in the background. The scene conveys trust and security.',
    'Депозит': 'An image of a person happily depositing money into a bank account. The background shows a bank interior with a sign indicating high-interest rates.',
    'Накопительный счет': 'An image of a person checking their savings account on a mobile app, with a graph showing increasing savings. The background shows a modern, tech-savvy environment.',
    'Дебетовая карта': 'An image of a person using a debit card at a point-of-sale terminal. The card has a sleek design, and the background shows a busy shopping area.',
    'Премиальная карта': 'An image of a luxurious credit card with a premium design, being used in an upscale setting like a fine dining restaurant or a luxury store.',
    'Брокерский и инвестиционный счет': 'An image of a person looking at stock charts and graphs on a computer screen. The background shows a modern office with financial news on a TV.',
    'Инвестиционное страхование жизни': 'An image of a family in a park, with a document showing a life insurance policy. They look secure and happy, with a bright future ahead.',
    'Накопительное страхование жизни': 'An image of a family at home, reviewing documents that represent a life insurance policy with savings benefits. They look content and secure.',
    'Страхование жизни': 'An image of a person holding an insurance policy document, with their family in the background. The scene conveys security and peace of mind.',
    'Доверительное управление': 'An image of a financial advisor discussing investment options with a client. The background shows charts and graphs indicating strong financial growth.',
    'Обезличенный металлический счет': 'An image of a gold bar and silver coins, with a document showing an unallocated metal account. The background conveys a sense of stability and wealth.',
    'Индивидуальный зарплатный проект': 'An image of a person happily receiving their salary via direct deposit. The background shows a modern office environment.',
    'Обмен валюты': 'An image of a person at a currency exchange counter, holding different currencies. The background shows a world map and exchange rate boards.'
}

SD = init_model(pathSD)


def add_generator(model, service):
    image = gen_logo(model, prompts[service])
    #image.save(f"back.png", "PNG")
    return image
