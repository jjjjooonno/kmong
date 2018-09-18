require(shiny)
library(rCharts)
runApp(list(
  ui = pageWithSidebar(
    headerPanel('Test'),
    sidebarPanel(  'Test'  ),
    mainPanel(
      chartOutput("Plot",'/Library/Frameworks/R.framework/Versions/3.4/Resources/library/rCharts/libraries')  
    )
  ),
  server = function(input, output, session){
    
    output$Plot <-  renderChart2({
      sankeyPlot2 <- rCharts$new()
      sankeyPlot2$setLib('/Library/Frameworks/R.framework/Versions/3.4/Resources/library/rCharts/libraries')
      sankeyPlot2$set(
        data = links,
        nodeWidth = 15,
        nodePadding = 10,
        layout = 32,
        width = 960,
        height = 500,
        units = "TWh",
        title = "Sankey Diagram"
      )
      return(sankeyPlot2)
    })
  }
))
