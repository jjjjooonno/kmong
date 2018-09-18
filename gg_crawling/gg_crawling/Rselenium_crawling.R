# sudo ln -f -s $(/usr/libexec/java_home)/jre/lib/server/libjvm.dylib /usr/local/lib
# rJava 오류시
# java -jar selenium-server-standalone-3.8.1.jar
# Rselenium server 구동 cmd 명령문
require(rvest)
require(RSelenium)
dr <- remoteDriver(remoteServerAddr = "localhost" 
                      , port = 4444
                      , browserName = "Chrome"
)
dr$open()
dr$navigate("http://www.kyeonggi.com/")
dr$findElement('xpath', '//*[@id="n_search_input"]')$sendKeysToElement(list('건축법',key = 'enter'))
news_crawler<- function(xpath1,xpath2,tag,news_holder){
  for (i in c(1:100)){
    dr$findElement('xpath',paste0(xpath1,as.character(i),xpath2))$sendKeysToElement(list(key = 'enter'))
    currWin <- dr$getCurrentWindowHandle()
    currWin
    allWins <- unlist(dr$getWindowHandles())
    allWins
    otherWindow <- allWins[!allWins %in% currWin[[1]]]
    dr$switchToWindow(otherWindow)
    pg<- dr$getPageSource()
    pg[[1]]
    ps<- read_html(pg[[1]])
    gisa<-html_nodes(ps, 'p')
    gisa
    cont<- html_text(gisa[[1]])
    news_holder<- c(news_holder,cont)
    
  }
}

dr$findElement('xpath',paste0('//*[@id="content"]/div[2]/div[2]/div[2]/div[',as.character(2),']/ul/li[1]/a'))$sendKeysToElement(list(key = 'enter'))
currWin <- dr$getCurrentWindowHandle()
currWin
allWins <- unlist(dr$getWindowHandles())
allWins
otherWindow <- allWins[!allWins %in% currWin[[1]]]
dr$switchToWindow(otherWindow)
dr$switchToWindow(currWin[[1]])
pg<- dr$getPageSource()
pg[[1]]
ps<- read_html(pg[[1]])

gisa<-html_nodes(ps, '#arl_view_content')
gisa
cont<- html_text(gisa[[1]])
cont

