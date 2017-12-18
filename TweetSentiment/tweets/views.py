from django.shortcuts import render
from .forms import SearchForm
import tweetSearch as tweetSearch
import tweetClassify as tweetClassify



# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
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

            
    else:
        form = SearchForm()
        tweets = []
        tweetSentimentPairs = []
        sentimentStats = ["N/A","N/A"]
        loadResults = False
        percent_neg = "N/A"
        percent_pos = "N/A"
    
    return render(request,'tweets/index.html',{'form':form,'tweets':tweets, 'pairs':tweetSentimentPairs, 'percent_neg':percent_neg,'percent_pos':percent_pos, 'loadResults':loadResults})


