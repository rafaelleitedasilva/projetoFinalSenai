// Pega os dados que estão dentro da div no html



var delayed;
{
    
    const ctx = document.getElementById('myChart').getContext("2d");
    let gradient = ctx.createLinearGradient(0,0,0,800);
    gradient.addColorStop(0,'rgb(138, 28, 28)');
    gradient.addColorStop(1,'rgb(220, 53, 69)');
    
    let labels = [
        'Elétrica',
        'Des. de Sistemas',
        'Ferramentaria',
    ];
    
    const data = {
        labels, 
        datasets: [{
            data:[99, 95, 90,],
            label:["Média por Curso"],
            fill: true,
            backgroundColor: gradient,
            borderColor: "#000",
            pointBackgroundcolor: "#000",
            tension: 0.5
        }]
    }
    
    
    const config = {
        type:'bar',
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
                    beginAtZero: true
                }
            }
        }
    }
    const myChart = new Chart(ctx, config);
    
}
{
    const ctx2 = document.getElementById('myChart2').getContext("2d");

    let labels = [
        'IDM',
        'PWFE',
        'PWBE',
        'BD',
    ];
    
    let gradient = ctx2.createLinearGradient(0,0,0,800);
    gradient.addColorStop(0,'rgb(138, 28, 28)');
    gradient.addColorStop(1,'rgb(220, 53, 69)');
    
    const data2 = {
        labels, 
        datasets: [{
            data:[89, 95, 100, 80],
            label:["Notas por matéria"],
            fill: true, 
            backgroundColor: gradient,
            borderColor: "#000",
            pointBackgroundcolor: "#000",
            tension: 0.5
        }]
    }
    const config2 = {
        type:'bar',
        data:data2,
        options: {
            indexAxis: 'y',
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
                    beginAtZero: true
                }
            }
        }
    }
    const myChart2 = new Chart(ctx2, config2);
}


{
    const ctx3 = document.getElementById('myChart3').getContext("2d");
    
    let labels = ['Aulas','Faltas']
    const data3 = {
        labels, 
        datasets: [{
            data:[300, 32],
            fill: true, 
            backgroundColor: ['rgb(138, 28, 28)','rgb(220, 53, 69)'],
        }]
    }
    
    const config3 = {
        type:'doughnut',
        data:data3,
        options: {
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
                    beginAtZero: true
                }
            }
        }
    }
    const myChart3 = new Chart(ctx3, config3);
}


{
    const ctx4 = document.getElementById('myChart4').getContext("2d");
    
    let gradient = ctx4.createLinearGradient(0,0,0,800);
    gradient.addColorStop(0,'rgb(220, 53, 69, 0.5)');
    gradient.addColorStop(1,'rgb(220, 53, 69, 0)');

    let labels = ['1° Termo','2° Termo','3° Termo']
    const data4 = {
        labels, 
        datasets: [{
            label:["Média final por Termo"],
            data:[98, 88, 90],
            fill: true, 
            backgroundColor: gradient,
            tension: 0.5,
            pointBackgroundcolor: "#000400",
        }]
    }
    
    const config4 = {
        type:'line',
        data:data4,
        options: {
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
            scales: {
                y: {
                    beginAtZero: true
                }
            }
            // Teste para transformação de dados (aqui no caso foi de centesimo para milhao)
        }
    }
    const myChart4 = new Chart(ctx4, config4);
}






// Constante que vai carregar todos os dados do gráfico 