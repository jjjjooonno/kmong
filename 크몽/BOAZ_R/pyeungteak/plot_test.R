library(ggplot2)

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
          '신장동',
          '신장동',
          '신평동',
          '원평동',
          '통복동',
          '비전동',
          '비전동',
          '세교동')
codes_not_dupl<- c('팽성읍',
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
                   '신장동',
                   '신장1동',
                   '신평동',
                   '원평동',
                   '통복동',
                   '비전동',
                   '비전1동',
                   '세교동')
SMshp= readShapePoly("bnd_dong_31070_2016.shp")
SMshp@data$ADM_NM<-factor(codes)
ptmap = fortify(SMshp)
ptmap$group<- factor(codes)
ggplot(data = ptmap, aes(x = long, y = lat, group = group)) + 
  geom_polygon()


dt_gong<- read.csv('gb_gong.csv',header = F)
dt_sil<- read.csv('gb_sil.csv', header = F)

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
dt_sil<- dt_gong[dt_sil$newdong %in% codes,]
data_2013<- dt_gong[dt_gong$year == 2013,]
codes_dt<- data.frame(codes)
colnames(codes_dt)<- 'newdong'
join_data<- join(codes_dt,data_2013,'newdong',type = "left")
final_price<- c()
for (e in join_data$price){
  if (is.na(e)){
    final_price<- c(final_price,0)
  }else{
    final_price<- c(final_price,e)
  }
}

dtt <- data.frame(cbind(final_price = final_price,codes))
levels(dtt$final_price)
SMshp@data$price<- final_price
SMshp@data$price_int<- as.integer(final_price)

qtm(SMshp , fill="price" , fill.style = "quantile" , fill.n = 22 , fill.palette = "Blues" , fill.title = "Pyungteak Map") + tm_text('price_int')
dtt$final_price<- as.numeric(as.character(dtt$final_price))
dtt$codes <- factor(dtt$codes, levels = dtt$codes_not_dupl[order(dtt$final_price,na.last = T)])
order(dtt$final_price,na.last = T)
dtt
levels = dtt$codes[order(dtt$final_price,na.last = T,decreasing = T)]
levels
ggplot(dtt)+
  geom_bar(stat = 'identity',mapping = aes(codes,final_price))
