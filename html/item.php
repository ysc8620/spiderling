<?php
$id = trim($_REQUEST['id']);
$conn = new Mongo();
$db = $conn->test;
$table = $db->goods;
error_reporting(E_ALL ^ E_NOTICE);
$row = $table->findOne(array('unique_id'=>$id));
?>
<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <title><?php echo $row['title'];?></title>
    <link rel="stylesheet" type="text/css" href="/html/css/base.css" />
    <link rel="stylesheet" type="text/css" href="/html/css/style.css" />
    <script src="/html/js/jquery.js"></script>
    <link rel="stylesheet" type="text/css" href="/html/css/item.css" />
</head>
<body>
<!--头部开始-->
<div class="header_wrap pt10">
    <div id="J_m_head" class="m_head clearfix">
        <div class="head_logo fl"><a href="test.php" class="logo_b fl" title="Shoplay">Shoplay</a></div>

    </div>
    <div id="J_m_nav" class="clearfix">
        <ul class="nav_list fl">
            <li><a href="test.php" class="current">Home</a></li>
            <li class="split "><a href="test.php?b=apple">Apple</a></li>
            <li class="split "><a href="test.php?c=food">food </a></li>
            <li class="split "><a href="test.php?q=iphone">iphone</a></li>
            <li class="split "><a href="test.php?q=chocolate">chocolate</a></li>
            <li class="top_search">
                <form action="test.php" method="get" target="_self">
                    <input type="text" autocomplete="off" def-val="" value="" class="ts_txt fl" name="q">
                    <input type="submit" class="ts_btn" value="Search">
                </form>
            </li>
        </ul>
    </div>
</div>
<!--商品详细-->
<div class="main_wrap pt10" style="_padding-left:0;">
<div class="mt10"><!--矩形广告位-->
</div>
<div class="itembox clearfix">
    <div class="itembox_l fl">
        <div class="note_box clearfix">
            <div id="J_item_gallery" class="show_body">
                <div class="J_item img_show">
                        <div id="J_img_zoom" class="img_zoom"><img alt="<?php echo $row['title'];?>" class="J_decode_img" data-uri="<?php echo base64_encode($row['img']);?>" src="<?php echo $row['img'];?>"></div>
                    <a href="javascript:;" class="J_joinalbum addalbum_btn" data-id="16"></a>
                </div>
                <div class="img_list clearfix">
                    <ul id="J_img_list" class="fl">
                        <?php foreach($row['img_list'] as $im):
                        ?>
                        <li data-url="<?php echo $im?>" class="active">
                            <img alt="<?php echo $row['title'];?>" class="J_decode_img" data-uri="<?php echo base64_encode($im);?>">                            </li>
                    <?php endforeach;?>
                    </ul>
                </div>
            </div>
                </div>
    </div>

    <div class="itembox_r fr">
        <div class="item_link mb20">
                <?php echo $row['title'];?></a>

        </div>
        <div>Brand: <a href="test.php?b=<?php echo $row['brand'];?>" target="brand"><?php echo $row['brand'];?></a> </div>
        <div>Category: <a href="test.php?b=<?php echo $row['category'];?>" target="category"><?php echo $row['category'];?></a> </div>
        <div><a href="<?php echo $row['from_url'];?>" rel="nofollow" target="_blank"><b>$<?php echo $row['price'];?> To from website</b><i></i></a></div>

        <!--矩形广告位-->
    </div>
</div>
<h3 class="may_fav_title mt20">详情.</h3>
<div class="wall_wrap clearfix">
<div id="J_waterfall" class="wall_container clearfix" >
<?php echo $row['description'];?>
</div>
 </div>
</div>

<div class="footer_wrap rt10">
    <a href="" class="foot_logo"></a>
    <div class="foot_links clearfix">
        <dl class="foot_nav fl">
            <dt>网站导航</dt>
            <dd><a href="test.php" >发现</a></dd><dd><a href="test.php" >专辑</a></dd><dd><a href="test.php" >集市</a></dd><dd><a href="test.php" >兑换</a></dd>        </dl>
        <dl class="aboutus fl">
            <dt>关于我们</dt>
            <dd><a href="?" target="_blank">关于我们</a></dd><dd><a href="test.php" target="_blank">联系我们</a></dd><dd><a href="#" target="_blank">加入我们</a></dd>        </dl>
        <dl class="flinks fr">
            <dt>友情链接</dt>
            <dd><a href="" target="_blank">Shoplay</a></dd><dd><a href="" class="more" target="_blank">更多...</a></dd>
        </dl>
        <dl class="followus fr">
            <dt>关注我们</dt>
            <dd><a href="" target="_blank">新浪微博</a></dd><dd><a href="/advert/tgo/id/26.html" target="_blank">腾讯微博</a></dd></dl>    </div>
    <p class="pt20">Powered by <a href="" class="tdu clr6" target="_blank">Shoplay</a> &copy;Copyright 2010-2012 </p>
</div>
<div id="J_returntop" class="return_top"></div>

<script type="text/javascript" src="/html/js/pinphp.js?20121126"></script>
</body>
</html>