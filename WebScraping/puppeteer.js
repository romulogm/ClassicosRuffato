// Acessar página individual do post, raspar e salvar dados, ir para a próxima página

const puppeteer = require('puppeteer');

(async () => {

const browser = await puppeteer.launch({ headless: false });
const page = await browser.newPage();
await page.goto('http://lendoosclassicosluizruffato.blogspot.com/2021/11/o-amigo-perdido-hella-haasse-1918-2011.html');

const reviewPost = {
  "title": "",
  "content": "",
  "avaliation": "",
  "author": "",
  "translator": "",
  "edition": ""
};

const stringIsIncluded = await page.evaluate(() => {
  const string = `#post-body-${postID}`;
  const selector = '#Blog1 > div.blog-posts.hfeed > div';
  return document.querySelector(selector).innerText.includes(string);
});

//Get post ID
const postMeta = await page.$("#Blog1 > div.blog-posts.hfeed > div > div > div > div.post.hentry.uncustomized-post-template > meta:nth-child(3)");
const postID = await page.evaluate(postMeta => postMeta.content, postMeta); 

// CONTENT
const content = await page.$(`#post-body-${postID} > span:nth-child(9) > p:nth-child(1)`);
const contentText = await page.evaluate(content => content.textContent, content); //or const text = await (await title.getProperty('textContent')).jsonValue();
reviewPost.content = contentText;

// TITLE
const title = await page.$(`#post-body-${postID} > p:nth-child(1) > span`);
const titleText = await page.evaluate(title => title.textContent, title);
reviewPost.title = titleText;

//AVALIATION 
const avaliation = await page.$(`#post-body-${postID} > span > p:nth-child(3) > b > span:nth-child(2)`);
const avaliationText = await page.evaluate(avaliation => avaliation.textContent, avaliation);
reviewPost.avaliation = avaliationText;

//FRONT COVER IMG

//AUTHOR 
const author = await page.$(`#post-body-${postID} > p:nth-child(2)`);
const authorText = await page.evaluate(author => author.textContent, author);
reviewPost.author = authorText;

//TRANSLATOR 
const translator = await page.$(`#post-body-${postID} > p:nth-child(3) > span:nth-child(1)`);
const translatorText = await page.evaluate(translator => translator.textContent, translator);
reviewPost.translator = translatorText;

//EDITION DATA 
const edition = await page.$(`#post-body-${postID} > p:nth-child(4) > span`);
const editionText = await page.evaluate(edition => edition.textContent, edition);
reviewPost.edition = editionText;

//GET NEXT LINK
const next = await page.$("#Blog1_blog-pager-older-link");
const nextHref = await page.evaluate(next => next.getAttribute("href"), next);


console.log(stringIsIncluded);
await browser.close();

})();


/*
const image = await page.$eval("div.separator > a > img", (image) =>
      image.getAttribute("src")
    );
const content = await page.$eval("span > p:nth-child(1) > span", el => el.innerText);     
const post = {
    title, 
    image, 
    content
  };
posts.push(post);
console.log(post);
*/
/*
let haveNext = false;
do {
  haveNext = false; 
  const button_next_page = await page.$("#Blog1_blog-pager-older-link"); 
  if (button_next_page) {
    await Promise.all(
      [
        page.waitForNavigation(),  
        page.$eval("#Blog1_blog-pager-older-link", e => e.click()) 
      ]
    );
    haveNext = true; 
  }
} while (haveNext);
*/