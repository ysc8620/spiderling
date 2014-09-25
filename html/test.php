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
</head>
<?php

$conn = new Mongo();
$db = $conn->test;
$table = $db->goods;
error_reporting(E_ALL ^ E_NOTICE);
require 'vendor/autoload.php';

$client = new Elasticsearch\Client(array("hosts"=>array("host"=>"54.255.39.86", "port"=>"9200")));

#$query  = new Elasticsearch\Elastica\Query();
$p = intval($_REQUEST['p']);
$p = $p<1?1:$p;

$searchParams['index'] = 'goods-index';
$searchParams['type']  = 'goods-type';
$searchParams['from'] = ($p - 1) * 20;
$searchParams['size'] = 20;
$searchParams['body']['sort'] = array(
    "title" => array(
        "order" => 'asc'
    )
);

$q = $_REQUEST['q'];
if($q){
    $searchParams['body']['query']['match']['title'] = $q;
}
$b = $_REQUEST['b'];
if($b){
    $searchParams['body']['query']['match']['brand'] = $b;
}

$c = $_REQUEST['c'];
if($c){
    $searchParams['body']['query']['match']['category'] = $c;
}

$queryResponse = $client->search($searchParams);

$total =  $queryResponse['hits']['total'];
// echo $total;
$total_page = ceil($total/20);

$data_list = array();
if(is_array($queryResponse)){
    foreach($queryResponse['hits']['hits'] as $item){
        $row = $table->findOne(array('unique_id'=>$item['_source']['unique_id']));
        $data_list[] = $row;
    }
}


function pagination($count,$perlogs,$page,$url){
    $pnums = @ceil($count / $perlogs);
    $sy = $page-1;
    $xy = $page+1;
    $re = '';
    for ($i = $page-3;$i <= $page+3 && $i <= $pnums; $i++){
        if ($i > 0){
            if ($i == $page){
                $re .= ' <span class="current">'.$i.'</span> ';
            } else {
                $re .= '<a href="'.$url.$i.'">'.$i.'</a>';
            }
        }
    }
    if ($page > 1) $re = '<a class="prev" href="'.$url.$sy.'" title="Previous page">Prev</a>'.$re;
    if ($page < $pnums) $re .= '<a class="prev" href="'.$url.$xy.'" title="Next page">Next</a>';
    if ($page+3 < $pnums) $re .= '<a class="prev" href="'.$url.$pnums.'" title="To end">End</a>';
    if ($pnums <= 1) $re = '';
    echo $re;
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
            <li><a href="?" class="current">Home</a></li>
            <li class="split "><a href="?b=apple">Apple</a></li>
            <li class="split "><a href="?c=food">food </a></li>
            <li class="split "><a href="?q=iphone">iphone</a></li>
            <li class="split "><a href="?q=chocolate">chocolate</a></li>
            <li class="top_search">
                <form action="" method="get" target="_self">
                    <input type="text" autocomplete="off" def-val="" value="" class="ts_txt fl" name="q">
                    <input type="submit" class="ts_btn" value="Search">
                </form>
            </li>
        </ul>
    </div>
</div>

<div class="main_wrap">
    <div class="wall_wrap clearfix">
        <div id="J_waterfall" class="wall_container clearfix" >

            <?php foreach($data_list as $item):?>
            <div class="J_item wall_item">
                <!--图片-->
                <ul class="pic">
                    <li>
                        <a href="item.php?id=<?php echo $item['unique_id'];?>" target="_blank">
                            <img alt="<?php echo $item['title'];?>" class="J_img J_decode_img" src="<?php echo ($item['img']);?>">
                        </a>
                        <span class="p">$<?php echo $item['price'];?></span>
                    </li>
                </ul>
                <!--说明-->
                <p class="intro clr6"><span class="goods_title"><?php echo $item['title'];?> </span><br />
                    <a href="?c=<?php echo $item['category'];?>" target="category"><?php echo $item['category'];?></a> &nbsp;  &nbsp; |  &nbsp;  &nbsp;
                    <a href="?b=<?php echo $item['brand'];?>" target="brand"><?php echo $item['brand'];?></a>
                </p>
                <!--评论-->
            </div>
            <?php endforeach;?>

            <div id="J_wall_loading" style="display: none" class="wall_loading tc gray"><span>加载中...</span></div>
            <div id="J_wall_page" class="wall_page" style="display: block!important;;">
                <div class="page_bar">
                    <?php
                    pagination($total, 20, $p, "?q=$q&b=$b&c=$c&p=");
                    ?>
                </div>
            </div>
        </div>

    </div>

    <div class="footer_wrap rt10">
        <a href="" class="foot_logo"></a>

        <div class="foot_links clearfix">
            <dl class="foot_nav fl">
                <dt>网站导航</dt>
                <dd><a href="?q=">发现</a></dd>
                <dd><a href="?q=">专辑</a></dd>
                <dd><a href="?q=">集市</a></dd>
                <dd><a href="?q=">兑换</a></dd>
            </dl>
            <dl class="aboutus fl">
                <dt>关于我们</dt>
                <dd><a href="?q=" >关于我们</a></dd>
                <dd><a href="?q=" >联系我们</a></dd>
                <dd><a href="?q=">加入我们</a></dd>
            </dl>
            <dl class="flinks fr">
                <dt>友情链接</dt>
                <dd><a href="?q=">Shoplay</a></dd>
                <dd><a href="?q=" class="more" >更多...</a></dd>
            </dl>
            <dl class="followus fr">
                <dt>关注我们</dt>
                <dd><a href="?q=" target="_blank">新浪微博</a></dd>
                <dd><a href="?q=" target="_blank">腾讯微博</a></dd>
            </dl>
        </div>
        <p class="pt20">Powered by <a href="" class="tdu clr6" target="_blank">Shoplay 3.0 20121126</a> &copy;Copyright 2010-2012 <a href="/" class="tdu clr6" target="_blank">Shoplay</a> (<a href="http://www.miibeian.gov.cn" class="tdu clr6" target="_blank">Shoplay</a>)</p>
    </div>
    <div id="J_returntop" class="return_top"></div>


</body>
</html>