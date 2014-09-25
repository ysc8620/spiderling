<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Shoplay</title>
    <meta name="keywords" content="Shoplay"/>
    <meta name="description" content="Shoplay"/>
    <link rel="stylesheet" type="text/css" href="/html/css/base.css"/>
    <link rel="stylesheet" type="text/css" href="/html/css/style.css"/>
    <script src="/html/js/jquery.js"></script>
</head><?php
$conn = new Mongo();
$db = $conn->test;
$table = $db->goods;

require 'vendor/autoload.php';

$client = new Elasticsearch\Client(array("hosts"=>array("host"=>"54.255.39.86", "port"=>"9200")));

#$query  = new Elasticsearch\Elastica\Query();

$searchParams['index'] = 'goods-index';
$searchParams['type']  = 'goods-type';
$searchParams['from'] = 0;
$searchParams['size'] = 12;
#$searchParams['body']['query']['match']['title'] = 'iphone';
$queryResponse = $client->search($searchParams);

$data_list = array();
if(is_array($queryResponse)){
    foreach($queryResponse['hits']['hits'] as $item){
        $row = $table->findOne(array('unique_id'=>$item['_id']));
        $data_list[] = $row;
    }
}
?>

<body>
<!--头部开始-->
<div class="header_wrap pt10">
    <div id="J_m_head" class="m_head clearfix">
        <div class="head_logo fl">Shoplay</div>
        <div class="head_user fr">
            <ul class="login_mod">

            </ul>
        </div>
    </div>
    <div id="J_m_nav" class="clearfix">
        <ul class="nav_list fl">
            <li><a href="/">首页</a></li>

            <li class="split current"><a href="/book/">发现</a></li>
            <li class="split "><a href="/album/">专辑</a></li>
            <li class="split "><a href="?m=book&a=cate&cid=1">集市</a></li>
            <li class="split "><a href="/ec/">兑换</a></li>
            <li class="split "><a href="?m=news">资讯</a></li>
            <li class="top_search">
                <form action="/" method="get" target="_blank">
                    <input type="hidden" name="m" value="search">
                    <input type="text" autocomplete="off" def-val="懒得逛了，我搜~" value="懒得逛了，我搜~" class="ts_txt fl"
                           name="q">
                    <input type="submit" class="ts_btn" value="搜索">
                </form>
            </li>
        </ul>
    </div>
</div>

<div class="main_wrap">


    <div class="wall_wrap clearfix">
        <div id="J_waterfall" class="wall_container clearfix" >
            <div class="J_item wall_tag">
                <h3>热门标签：</h3>
                <div class="tags clearfix">
                    <a href="">全部</a>
                    <a href="">性感</a></div>
                <!--矩形广告位-->
            </div>
            <?php foreach($data_list as $item):?>
            <div class="J_item wall_item">
                <!--图片-->
                <ul class="pic">
                    <li>
                        <a href="">
                            <img alt="<?php echo $item['title'];?>" class="J_img J_decode_img" data-uri="<?php echo base64_encode($item['img']);?>">
                        </a>
                        <span class="p">$<?php echo $item['price'];?></span>
                        <a href=""></a>
                    </li>
                </ul>
                <!--说明-->
                <p class="intro clr6"><?php echo $item['title'];?></p>
                <!--评论-->
            </div>
            <?php endforeach;?>

            <div id="J_wall_loading" class="wall_loading tc gray"><span>加载中...</span></div>
            <div id="J_wall_page" class="wall_page">
                <div class="page_bar"><a href='/book/p3'><</a> <a href='/book/p1'>1</a> <i>...</i> <a href='/book/p2'>
                    &nbsp;2&nbsp;</a> <a href='/book/p3'>&nbsp;3&nbsp;</a> <span class='current'>4</span> <a
                        href='/book/p5'>&nbsp;5&nbsp;</a> <a href='/book/p6'>&nbsp;6&nbsp;</a> <i>...</i> <a
                        href='/book/p10'>10</a> <a href='/book/p5'>下一页></a></div>
            </div>
        </div>

    </div>

    <div class="footer_wrap rt10">
        <a href="" class="foot_logo"></a>

        <div class="foot_links clearfix">
            <dl class="foot_nav fl">
                <dt>网站导航</dt>
                <dd><a href="/book/">发现</a></dd>
                <dd><a href="/album/">专辑</a></dd>
                <dd><a href="?m=book&a=cate&cid=1">集市</a></dd>
                <dd><a href="/ec/">兑换</a></dd>
            </dl>
            <dl class="aboutus fl">
                <dt>关于我们</dt>
                <dd><a href="/aboutus/index/id/2.html" target="_blank">关于我们</a></dd>
                <dd><a href="/aboutus/index/id/3.html" target="_blank">联系我们</a></dd>
                <dd><a href="/aboutus/index/id/4.html" target="_blank">加入我们</a></dd>
            </dl>
            <dl class="flinks fr">
                <dt>友情链接</dt>
                <dd><a href="http://www.pinphp.com" target="_blank">PinPHP</a></dd>
                <dd><a href="/aboutus/flink.html" class="more" target="_blank">更多...</a></dd>
            </dl>
            <dl class="followus fr">
                <dt>关注我们</dt>
                <dd><a href="/advert/tgo/id/25.html" target="_blank">新浪微博</a></dd>
                <dd><a href="/advert/tgo/id/26.html" target="_blank">腾讯微博</a></dd>
            </dl>
        </div>
        <p class="pt20">Powered by <a href="" class="tdu clr6" target="_blank">PinPHP 3.0
            20121126</a> &copy;Copyright 2010-2012 <a href="/" class="tdu clr6" target="_blank">拼品网</a> (<a
                href="http://www.miibeian.gov.cn" class="tdu clr6" target="_blank">浙ICP备10202542号</a>)</p>
    </div>
    <div id="J_returntop" class="return_top"></div>

    <script>
        var PINER = {
            root:"",
            uid:"",
            async_sendmail:"",
            config:{
                wall_distance:"500",
                wall_spage_max:"1"
            },
            //URL
            url:{}
        };
        //语言项目
        var lang = {};
        lang.please_input = "请输入";
        lang.username = "用户名";
        lang.password = "密码";
        lang.login_title = "用户登陆";
        lang.share_title = "我要分享";
        lang.correct_itemurl = "正确的商品地址";
        lang.join_album = "加入专辑";
        lang.create_album = "创建新专辑";
        lang.edit_album = "修改专辑";
        lang.confirm_del_album = "删除专辑，专辑里所有的图片都会被删除哦！你确定要删除此专辑吗？";
        lang.title = "标题";
        lang.card_loading = "正在获取用户信息";
        lang.confirm_unfollow = "确定要取消关注么？";
        lang.wait = "请稍后......";</script>
    <script type="text/javascript" src="/html/js/pinphp.js?20121126"></script>
</body>
</html>