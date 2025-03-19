
from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

# Create the chatbot instance
bot = ChatBot(
    'chatbot',
    read_only=False,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            # 'default_response': 'I am sorry, but I do not understand.',
            # 'maximum_similarity_threshold':0.95
        
        }])

# Train the chatbot
List_to_train=[
    "hi",
    "hi, there",
    "what's your name",
    "I'm chatbot",
    "what is your favorite food",
    "I like pizza"
]

chatterbotCorposTrainer=ChatterBotCorpusTrainer(bot)

chatterbotCorposTrainer.train(
    'chatterbot.corpus.english'
)
# Django views
def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse('list1')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)  # Return bot response instead of user input
    

