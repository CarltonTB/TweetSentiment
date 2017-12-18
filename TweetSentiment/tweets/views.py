from django.shortcuts import render
from .forms import SearchForm
import tweetSearch as tweetSearch
import tweetClassify as tweetClassify
# from .forms import ClassifyForm



# Create your views here.

def index(request):
#     form2=ClassifyForm()
    form = SearchForm()
    tweets = []
    tweetSentimentPairs = []
    sentimentStats = ["N/A","N/A"]
    loadResults = False
    percent_neg = "N/A"
    percent_pos = "N/A"
    text = ""
    textClassification = ""
    if request.method == 'POST':
        form = SearchForm(request.POST)
#         form2 = ClassifyForm(request.POST)
        if form.is_valid():
            if len(str(form.cleaned_data)) > 0:
                searchTerm = str(form.cleaned_data['query'])
                #pass the classified tweets to the page for populating the table
                tweets = tweetSearch.getTweets(100,searchTerm)
                tweetSentimentPairs = tweetClassify.classifyTweets(tweets,searchTerm)
                sentimentStats = tweetClassify.computeSentimentStats(tweetSentimentPairs)
                percent_neg = sentimentStats[0]
                percent_pos = sentimentStats[1]
                loadResults = True

#         if form2.is_valid():
#             textClassification = tweetClassify.classifySentiment(form2.cleaned_data['text'])
#             text = form2.cleaned_data['text']
#'classifyForm': form2, 'text': text, 'textClassification':textClassification,  
    
    return render(request,'tweets/index.html',{'searchForm':form,' tweets':tweets, 'pairs':tweetSentimentPairs, 'percent_neg':percent_neg,'percent_pos':percent_pos, 'loadResults':loadResults})


