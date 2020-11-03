var ec_center = echarts.init(document.getElementById('c2'));

// var mydata = [{'name': 'Pennsylvania', 'value': 318}, {'name': 'New Jersey', 'value': 162}]

var ec_center_option = {
    title: {
        text: '',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },

    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 10,
        },
        splitList: [{ start: 1,end: 100000 },
            {start: 100000, end: 200000 },
			{ start: 200000, end: 300000 },
            {  start: 300000, end: 500000 },
            { start: 500000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },

    series: [{
        name: 'confirmed',
        type: 'map',
        mapType: 'USA',
        roam: true,
        itemStyle: {
            normal: {
                borderWidth: .5,
                borderColor: '#009fe8',
                areaColor: "#ffefd5",
            },
            emphasis: {
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true,
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data: []
    }]
};
ec_center.setOption(ec_center_option)