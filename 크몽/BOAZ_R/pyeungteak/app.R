library("ggplot2")
library("ggmap")
library("sp")
library("maptools")
library('tmap')
library('plyr')
library('sf')
library('rmapshaper')
library('RColorBrewer')
library('shiny')
library('readxl')
library('extrafont')
library('plotly')
library(flexdashboard)
library(ggplot2)
library(dygraphs)
library(crosstalk)
library(highcharter)
library(rAmCharts)
# font_import(pattern = 'Apple')
ui <- fluidPage(
  titlePanel("평택시 공시지가 & 실거래가"),
  sidebarLayout(
    sidebarPanel(
      selectInput('year', '연도 선택', c(2013,2014,2015,2016)),
      actionButton("go", "완료"),
      helpText('보고싶은 연도를 선택한 후 완료를 눌러주세요.')
    ),
    mainPanel(
      tabsetPanel(
        tabPanel("공시지가 지도", plotOutput("mymap_gong")),
        tabPanel("실거래가 지도", plotOutput("mymap_sil")),
        tabPanel("공시지가 막대그래프 보기", plotlyOutput('bar1')),
        tabPanel("실거래가 막대그래프 보기", plotlyOutput('bar2'))
      )
    )
  )
)

server <- function(input, output) {
  dt <- eventReactive(input$go,{
    codes<- c('팽성읍',
              '안중읍',
              '포승읍',
              '청북읍',
              '진위면',
              '서탄면',
              '고덕면',
              '오성면',
              '현덕면',
              '중앙동',
              '서정동',
              '송탄동',
              '지산동',
              '송북동',
              '신장1동',
              '신장2동',
              '신평동',
              '원평동',
              '통복동',
              '비전1동',
              '비전2동',
              '세교동')
    SMshp <- readShapePoly("bnd_dong_31070_2016.shp")
    SMshp@data$ADM_NM<-factor(codes)
    dt_gong<- read_excel('gb_gong.xlsx')
    dt_sil<- read_excel('gb_sil.xlsx')
    
    colnames(dt_gong) <- c('year','dong','price')
    colnames(dt_sil) <- c('year','dong','price')
    dongs_gong= c()
    for (i in dt_gong$dong){
      if (i == '비전동'){
        dongs_gong <- c(dongs_gong, '비전1동')
      }else{
        if (i == '신장동'){
          dongs_gong <- c(dongs_gong, '신장1동')
        }else{
          dongs_gong <- c(dongs_gong, i)
        }
      }
    }
    dongs_sil= c()
    for (i in dt_sil$dong){
      if (i == '비전동'){
        dongs_sil <- c(dongs_sil, '비전1동')
      }else{
        if (i == '신장동'){
          dongs_sil <- c(dongs_sil, '신장1동')
        }else{
          dongs_sil <- c(dongs_sil, i)
        }
      }
    }
    dt_gong$newdong<- factor(dongs_gong)
    dt_sil$newdong<- factor(dongs_sil)
    dt_gong<- dt_gong[dt_gong$newdong %in% codes,]
    dt_sil<- dt_sil[dt_sil$newdong %in% codes,]
    data_gong<- dt_gong[dt_gong$year == input$year,]
    data_sil<- dt_sil[dt_sil$year == input$year,]
    
    codes_dt<- data.frame(codes)
    colnames(codes_dt)<- 'newdong'
    join_data_gong<- join(codes_dt,data_gong,'newdong',type = "left")
    join_data_sil<- join(codes_dt,data_sil,'newdong',type = "left")
    final_price_gong<- c()
    for (e in join_data_gong$price){
      if (is.na(e)){
        final_price_gong<- c(final_price_gong,0)
      }else{
        final_price_gong<- c(final_price_gong,as.integer(e))
      }
    }
    SMshp@data$price_gong<-final_price_gong
    final_price_sil<- c()
    for (e in join_data_sil$price){
      if (is.na(e)){
        final_price_sil<- c(final_price_sil,0)
      }else{
        final_price_sil<- c(final_price_sil,as.integer(e*10000))
      }
    }
    SMshp@data$price_sil<-final_price_sil
    return(SMshp)
  })
  dtt <- eventReactive(input$go,{
    dt_gong<- read_excel('gb_gong.xlsx')
    dt_sil<- read_excel('gb_sil.xlsx')
    
    colnames(dt_gong) <- c('year','dong','price')
    colnames(dt_sil) <- c('year','dong','price')
    dongs_gong= c()
    for (i in dt_gong$dong){
      if (i == '비전동'){
        dongs_gong <- c(dongs_gong, '비전1동')
      }else{
        if (i == '신장동'){
          dongs_gong <- c(dongs_gong, '신장1동')
        }else{
          dongs_gong <- c(dongs_gong, i)
        }
      }
    }
    dongs_sil= c()
    for (i in dt_sil$dong){
      if (i == '비전동'){
        dongs_sil <- c(dongs_sil, '비전1동')
      }else{
        if (i == '신장동'){
          dongs_sil <- c(dongs_sil, '신장1동')
        }else{
          dongs_sil <- c(dongs_sil, i)
        }
      }
    }
    dt_gong$newdong<- factor(dongs_gong)
    dt_sil$newdong<- factor(dongs_sil)
    dt_gong<- dt_gong[dt_gong$newdong %in% codes,]
    dt_sil<- dt_sil[dt_sil$newdong %in% codes,]
    data_gong<- dt_gong[dt_gong$year == input$year,]
    data_sil<- dt_sil[dt_sil$year == input$year,]
    
    codes_dt<- data.frame(codes)
    colnames(codes_dt)<- 'newdong'
    join_data_gong<- join(codes_dt,data_gong,'newdong',type = "left")
    join_data_sil<- join(codes_dt,data_sil,'newdong',type = "left")
    final_price_gong<- c()
    for (e in join_data_gong$price){
      if (is.na(e)){
        final_price_gong<- c(final_price_gong,0)
      }else{
        final_price_gong<- c(final_price_gong,as.integer(e))
      }
    }
    SMshp@data$price_gong<-final_price_gong
    final_price_sil<- c()
    for (e in join_data_sil$price){
      if (is.na(e)){
        final_price_sil<- c(final_price_sil,0)
      }else{
        final_price_sil<- c(final_price_sil,as.integer(e*10000))
      }
    }
    dtt <- data.frame(cbind(final_price_sil,final_price_gong,codes))
    dtt$final_price_sil<- as.integer(as.character(dtt$final_price_sil))
    dtt$final_price_gong<- as.integer(as.character(dtt$final_price_gong))
    return(dtt)
  })
  output$mymap_gong <- renderPlot({
    qtm(dt() , fill="price_gong" , fill.style = "quantile" , fill.n = 16 , fill.palette = "Reds" , fill.title = "서울 지도")+
      tm_text('price_gong')+
      tm_layout(legend.outside = TRUE, legend.outside.position = "right", legend.stack = "horizontal")
  })
  output$mymap_sil <- renderPlot({
    qtm(dt() , fill="price_sil" , fill.style = "quantile" , fill.n = 16 , fill.palette = "Reds" , fill.title = "서울 지도")+
      tm_text('price_sil')+
      tm_layout(legend.outside = TRUE, legend.outside.position = "right", legend.stack = "horizontal")
  })
  output$bar1<- renderPlotly({
    p<-ggplot(dtt(),aes(x=reorder(dtt()$codes,dtt()$final_price_gong),y=final_price_gong))+
      geom_bar(stat = "summary",fill = "#FF6666")+
      coord_flip()+
      ylab(paste0(as.character(input$year),'년 공시지가'))+
      xlab('.')+
      coord_flip(ylim = c(100000,1500000))+
      geom_text(aes(label=final_price_gong), vjust=0)
    ggplotly(p)
  })
  output$bar2<- renderPlotly({
    p2<-ggplot(dtt(),aes(x=reorder(dtt()$codes,dtt()$final_price_sil),y=final_price_sil))+
      geom_bar(stat = "summary",fill = "#FF6666")+
      coord_flip()+
      ylab(paste0(as.character(input$year),'년 공시지가'))+
      xlab('.')+
      coord_flip(ylim = c(100000,1900000))+
      geom_text(aes(label=final_price_sil), vjust=0)
    ggplotly(p2)
  })
}

# Run the application 
shinyApp(ui = ui, server = server)