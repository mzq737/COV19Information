var ec_right1 = echarts.init(document.getElementById('r1'));
var ec_right1_option = {
	title : {
	    text : "Cases TOP 5 states",
	    textStyle : {
	        color : 'white',
	    },
	    left : 'left'
	},
	grid: {
		left: '0%',
		right: '4%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	  color: ['#D6823B'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {
	            type: 'shadow'
	        }
	    },
    xAxis: [{
        type: 'category',
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 10,
		},
		data: []
    }],
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%"
    }]
};
ec_right1.setOption(ec_right1_option)