
Create env
python -m venv scrapy-env
Activate 
scrapy-env\Scripts\activate


scrapy shell http://lendoosclassicosluizruffato.blogspot.com/2021/09/tempestades-de-aco-1920-ernst-junger.html
scrapy crawl lendoclassicos -o test.csv


Links Extraction: 

(?=(?:[^"]*"[^"]*")*[^"]*$)

var postsLists = document.querySelectorAll('ul.posts');
if (postsLists.length > 0) {
  postsLists.forEach(function(postsList) {
    var content = postsList.innerHTML;
    console.log(content);
  });
} else {
  console.log('No <ul> elements with class "posts" found.');
}