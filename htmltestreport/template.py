class Template(object):
    """
    测试报告模板
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: u'通过',
        1: u'失败',
        2: u'错误',
        3: u'跳过',
    }

    DEFAULT_TITLE = '测试报告'
    DEFAULT_DESCRIPTION = ''

    # HTML Template
    # variables: (title, generator, stylesheet, heading, report, ending, chart_script)
    HTML_TMPL = r"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <link rel="stylesheet" href="http://unpkg.com/layui@2.6.8/dist/css/layui.css">
    %(stylesheet)s
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
</head>
<body>
    <script language="javascript" type="text/javascript"><!--
    output_list = Array();
    function showCase(level) {
        trs = document.getElementsByTagName("tr");
        for (var i = 0; i < trs.length; i++) {
            tr = trs[i];
            id = tr.id;
            if (id.substr(0,2) == 'ft') {
                if (level == 2 || level == 0) {
                    tr.className = 'hiddenRow';
                }
                else {
                    tr.className = '';
                }
            }
            if (id.substr(0,2) == 'pt') {
                if (level < 2) {
                    tr.className = 'hiddenRow';
                }
                else {
                    tr.className = '';
                }
            }
        }      
    }
    function showClassDetail(cid, count) {
        var id_list = Array(count);
        var toHide = 1;
        for (var i = 0; i < count; i++) {
            tid0 = 't' + cid.substr(1) + '.' + (i+1);
            tid = 'f' + tid0;
            tr = document.getElementById(tid);
            if (!tr) {
                tid = 'p' + tid0;
                tr = document.getElementById(tid);
            }
            id_list[i] = tid;
            if (tr.className) {
                toHide = 0;
            }
        }
        for (var i = 0; i < count; i++) {
            tid = id_list[i];
            if (toHide) {
                document.getElementById(tid).className = 'hiddenRow';
            }
            else {
                document.getElementById(tid).className = '';
            }
        }
    }
    function showTestDetail(div_id){
        var details_div = document.getElementById(div_id)
        var displayState = details_div.style.display
        if (displayState == 'block' || displayState == '' ) {
            details_div.style.display = 'none'
        }
        else {
            displayState = 'block'
            details_div.style.display = 'block'
        }
    }
    function html_escape(s) {
        s = s.replace(/&/g,'&amp;');
        s = s.replace(/</g,'&lt;');
        s = s.replace(/>/g,'&gt;');
        return s;
    }
    --></script>
    <div class="layui-container">
        %(heading)s
        %(report)s
        %(ending)s
        %(chart_script)s
    </div>
</body>
</html>
"""

    # 图表
    # variables: (Pass, fail, error)
    ECHARTS_SCRIPT = r"""
    <script type="text/javascript">
        // 初始化echarts实例
        var myChart1 = echarts.init(document.getElementById('chart1'));
        var myChart2 = echarts.init(document.getElementById('chart2'));
        // 指定图表的配置项和数据
        option1 = {
            tooltip: {
                formatter: '{a} <br/>{b} : {c}%%'
            },
            toolbox: {
                feature: {
                    restore: {},
                    saveAsImage: {}
                }
            },
            series: [{
                name: '测试结果',
                type: 'gauge',
                detail: {
                    formatter: '%(passrate)s%%'
                },
                data: [{
                    value: '%(passrate)s',
                    name: '用例通过率'
                }],
                axisLine: {
                    lineStyle: {
                        color: [
                            [0.2, '#c20000'],
                            [0.8, '#ddb518'],
                            [1, '#00a10a']
                        ]
                    }
                }
            }]
        };
        option2 = {
            color: ['#00a10a', '#ddb518', 'rgba(204,46,41,0.73)', '#85898c'],
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%%)'
            },
            legend: {
                orient: 'vertical',
                left: 10,
                data: ['通过', '失败', '错误', '跳过']
            },
            series: [{
                name: '测试结果',
                type: 'pie',
                radius: ['50%%', '70%%'],
                avoidLabelOverlap: false,
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '30',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [{
                        value: %(Pass)s,
                        name: '通过'
                    },
                    {
                        value: %(fail)s,
                        name: '失败'
                    },
                    {
                        value: %(error)s,
                        name: '错误'
                    },
                    {
                        value: %(skip)s,
                        name: '跳过'
                    }
                ]
            }]
        };

        myChart1.setOption(option1);
        myChart2.setOption(option2);
    </script>
    """

    # Stylesheet
    STYLESHEET_TMPL = """
<style type="text/css">
    .title { width: auto; height: 60px; text-align: center; font: bolder 38px/60px "Microsoft YaHei UI"; color: #009688; }
    .summary span { font: normal 16px/38px "Microsoft YaHei UI"; margin-left: 20px; }
    .success-btn { background-color: #28a745; }
    .skip-btn { background-color: #84898c; }
    .passClass  { background-color: #bdedbc; }
    .failClass  { background-color: #ffefa4; }
    .errorClass { background-color: #ffc9c9; }
    .passCase   { color: #5cb85c; }
    .skipCase   { color: #84898c; }
    .failCase   { color: #FF6600; font-weight: bold; }
    .errorCase  { color: #c00; font-weight: bold; }
    .hiddenRow  { display: none; }
    .testcase   { margin-left: 2em; }
    .layui-table tbody tr:hover, .layui-table-click, .layui-table-header, .layui-table-hover, .layui-table-mend, .layui-table-patch, .layui-table-tool, .layui-table[lay-even] tr:nth-child(even) {
        background-color: transparent;
    }
</style>
"""

    # Heading
    HEADING_TMPL = r"""
    <!--报告标题-->
    <div class="title">%(title)s</div>
    
    <!--汇总信息-->
    <fieldset class="layui-elem-field summary">
        <legend>测试结果汇总</legend>
        <div class="layui-field-box">
            <table class="layui-table">
                <colgroup>
                    <col width="50%%">
                    <col width="50%%">
                </colgroup>
                <tbody>
                    <tr>
                        <td>
                            <button type="button" class="layui-btn">开始时间</button>
                            <span class="text-dark">%(start_time)s</span>
                        </td>
                        <td>
                            <button type="button" class="layui-btn">执行时间</button>
                            <span class="text-dark">%(duration)s s</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <button type="button" class="layui-btn">用例总数</button>
                            <span class="text-dark">%(total_count)s</span>
                        </td>
                        <td>
                            <button type="button" class="layui-btn">通过率</button>
                            <span class="text-dark">%(passrate)s%%</span>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <button type="button" class="layui-btn">描述信息</button>
                            <span class="text-dark">%(description)s</span>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2" align="center">
                            <button type="button" class="layui-btn success-btn">成功用例：%(success_count)s</button>
                            <button type="button" class="layui-btn layui-btn-warm">失败用例：%(failure_count)s</button>
                            <button type="button" class="layui-btn layui-btn-danger">错误用例：%(error_count)s</button>
                            <button type="button" class="layui-btn skip-btn">跳过用例：%(skip_count)s</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </fieldset>
    
    <!--图表展示-->
    <fieldset class="layui-elem-field summary">
        <legend>图表展示</legend>
        <div class="layui-field-box">
            <div class="char">
                <div id="chart1" style="width: 49%%;height: 400px;float: left"></div>
                <div id="chart2" style="width: 49%%;height: 400px;float: left"></div>
            </div>
        </div>
    </fieldset>
"""

    # Report
    # variables: (test_list, count, Pass, fail, error, passrate)
    REPORT_TMPL = u"""
    <fieldset class="layui-elem-field summary">
        <legend>详细信息</legend>
        <div class="layui-field-box">
            <table id='result_table' class="layui-table">
            <thead>
                <tr id='header_row' style='background-color: #009688; color: #fff'>
                    <th>测试用例</th>
                    <th>总数</th>
                    <th>通过</th>
                    <th>失败</th>
                    <th>错误</th>
                    <th>跳过</th>
                    <th>操作</th>
                </tr>
                </thead>
				<tbody>
                %(test_list)s
                </tbody>
                <tr id='total_row' class="text-center active">
                    <td align="right">总计</td>
                    <td>%(count)s</td>
                    <td>%(Pass)s</td>
                    <td>%(fail)s</td>
                    <td>%(error)s</td>
                    <td>%(skip)s</td>
                    <td></td>
                </tr>
            </table>
        </div>
	</fieldset>
"""

    # variables: (style, desc, count, Pass, fail, error, cid)
    REPORT_CLASS_TMPL = u"""
    <tr class='%(style)s'>
        <td class="text-center">%(desc)s</td>
        <td class="text-center">%(count)s</td>
        <td class="text-center">%(Pass)s</td>
        <td class="text-center">%(fail)s</td>
        <td class="text-center">%(error)s</td>
        <td class="text-center">%(skip)s</td>
        <td class="text-center"><button type="button" class="layui-btn layui-btn-xs" onclick="showClassDetail('%(cid)s',%(count)s)">详细</button></td>
    </tr>
"""

    # variables: (tid, Class, style, desc, status)
    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td>
    <a onfocus='this.blur();' data-toggle="collapse" href="javascript:showTestDetail('div_%(tid)s')">
        %(status)s</a>
    </td>
    <td colspan='5'>
    <div id='div_%(tid)s' class="collapse in">
        <blockquote class="layui-elem-quote">
            <pre>%(script)s</pre>
        </blockquote>
    </div>
    </td>
</tr>
"""

    # variables: (tid, Class, style, desc, status)
    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td>%(status)s</td>
    <td colspan='5' align='center' style="color:#428bca"></td>
</tr>
"""

    REPORT_TEST_OUTPUT_TMPL = r"""%(id)s: %(output)s"""  # variables: (id, output)

    # ENDING
    ENDING_TMPL = """<a href="#">
    <ul class="layui-fixbar"><li class="layui-icon layui-fixbar-top" lay-type="top" style="display: list-item;"></li></ul>
    </a>
    """
