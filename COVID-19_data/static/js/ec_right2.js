var ec_right2 = echarts.init(document.getElementById('r2'));

var ec_right2_option = {
    title : {
        text : "Trending Cov19 Questions Keywords in Google",
        textStyle : {
            color : 'white',
        },
        left : 'left'
    },
    tooltip: {
        show: false
    },
    series: [{
            type: 'wordCloud',
            // drawOutOfBound:true,
            gridSize: 1,
            sizeRange: [12, 55],
            rotationRange: [-45, 0, 45, 90],
            // maskImage: maskImage,
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' +
                                Math.round(Math.random() * 255) +
                                ', ' + Math.round(Math.random() * 255) +
                                ', ' + Math.round(Math.random() * 255) + ')'
                    }
                }
            },

            right: null,
            bottom: null,
            data:  []
        }]
}

ec_right2.setOption(ec_right2_option);
