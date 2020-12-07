var ec_left2 = echarts.init(document.getElementById('l2'));
var ec_left2_Option = {
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['New Cases', 'New Deaths'],
		left: "right"
	},
	title: {
		text: "",
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
	grid: {
		left: '7%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		data: []
	}],
	yAxis: [{
		type: 'value',
		axisLine: {
			show: true
		},
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 12,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [{
		name: "New Cases",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "New Deaths",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_left2.setOption(ec_left2_Option)
