// Pega os dados que estão dentro da div no html
const ctx = document.getElementById('myChart').getContext("2d");

let delayed;

// Variavel de cor
let gradient = ctx.createLinearGradient(0,0,0,800);
gradient.addColorStop(0,'rgb(138, 28, 28)');
gradient.addColorStop(1,'rgb(220, 53, 69)');

// Parametros que vao na parte de baixo do grafico 
const labels = [
    '2012',
    '2013',
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019',
    '2020',
];

// Dados gerais do grafico 
const data = {
    labels, 
    datasets: [{
        data:[211, 326, 358, 459, 111, 333, 543, 976, 345,],
        label:["Teste maluco"],
        fill: true,
        backgroundColor: gradient,
        borderColor: "#000",
        pointBackgroundcolor: "#000",
        tension: 0.5
    }]
}

const config = {
    type:'line',
    data:data,
    options: {
        radius: 5,
        hitRadius: 30,
        hoverRadius: 12,
        responsive:true,
        animation:{
            onComplete: () => {
                delayed = true;
            },
            delay: (context) => {
                let delay = 0;
                if(context.type === "data" && context.mode === "default" && !delayed){
                    delay = context.dataIndex * 300 + context.datasetIndex * 100;
                }
                return delay;
            },
        },
        // Teste para transformação de dados (aqui no caso foi de centesimo para milhao)
        scales: {
            y: {
                ticks:{
                    callback: function(value){
                        return '$' + value + "m";
                    }
                }
            }
        }
    }
}

// Constante que vai carregar todos os dados do gráfico 
const myChart = new Chart(ctx, config);


