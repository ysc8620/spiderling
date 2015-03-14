# coding: utf-8
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/$", deny=r".*?(model=list|dir=)")),
# #Rule(LinkExtractor(allow=r"http://www.lazada.sg/.+/(\?page=\d+)?$", deny=r".*?(new\-products|top\-sellers|special\-price)")),
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(fun|tech|wellness|food|tavel|home|family|fashion)(/(indoo|outdoo|compute-accessoies|camea-accessoies|mobile-accessoies|skin-cae|cosmetics|accessoies|beauty-sevices|tickets|tavelaccessoies|appliances|watches|household|bags-and-wallets|ladies|men-s))?(\?p=\d+)?$", deny=r".*?(model=list|dir=)")),
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(fun|tech|wellness|tavel|home|fashion)/(indoo|outdoo|compute-accessoies|camea-accessoies|mobile-accessoies|skin-cae|cosmetics|accessoies|beauty-sevices|tickets|tavelaccessoies|appliances|watches|household|bags-and-wallets|ladies|men-s)/\w+$"), callback='parse_item'),
# Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(family|food)/\w+$"), callback='parse_item'),

from spider.items import DealItem
from spider.tools.matchfield import match_dmoz_field
from scrapy.selector import Selector
import time
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

html = u'''



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>


<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<!--<meta http-equiv="X-UA-Compatible" content="IE=9" />--> <!--Nang Added for IE 9-->
<title>Mistral Power 3x6inch Fan - Home</title>
<meta name="description" content="&lt;p&gt;&lt;span style=&quot;text-decoration: underline; font-size: small;&quot;&gt;&lt;strong&gt;Terms and Conditions&lt;/strong&gt;&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;Return Policy:&lt;br /&gt;&lt;span&gt;Voucher is valid within 2 months upon purchase.&lt;/span&gt;&lt;br /&gt;We offer 1 for 1 exchange for items with manufactu" />
<meta name="keywords" content="Mistral Power 3x6inch Fan" />
<meta name="robots" content="INDEX,FOLLOW" />
<link rel="icon" href="https://www.imobshop.sg/media/favicon/default/favicon_org.ico" type="image/x-icon" />
<link rel="shortcut icon" href="https://www.imobshop.sg/media/favicon/default/favicon_org.ico" type="image/x-icon" />

<!--[if lt IE 7]>
<script type="text/javascript">
//<![CDATA[
    var BLANK_URL = 'https://www.imobshop.sg/js/blank.html';
    var BLANK_IMG = 'https://www.imobshop.sg/js/spacer.gif';
//]]>
</script>
<![endif]-->
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/js/calendar/calendar-win2k-1.css" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/css/styles.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/base/default/css/widgets.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/marketplace/marketplace.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/default/css/belvg/facebookfree.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/cinderella/cinderella.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/base/default/css/j2t-rewardpoints.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/webandpeople/custommenu/custommenu.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/css/responsive.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/css/nav.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/ajaxcart/js/fancybox/jquery.fancybox-1.3.4.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/ajaxcart/css/styles.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/base/default/css/jqzoom.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/cloud-zoom/css/cloud-zoom.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/bxslider/css/jquery.bxslider.css" media="all" />
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/css/print.css" media="print" />
<script type="text/javascript" src="https://www.imobshop.sg/js/prototype/prototype.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/lib/ccard.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/prototype/validation.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/scriptaculous/builder.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/scriptaculous/effects.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/scriptaculous/dragdrop.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/scriptaculous/controls.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/scriptaculous/slider.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/varien/js.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/varien/form.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/varien/menu.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/mage/translate.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/mage/cookies.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/varien/product.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/varien/configurable.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/calendar/calendar.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/calendar/calendar-setup.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/CBjquery/jquery-1.5.2.min.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/CBjquery/jquery.jqzoom1.0.1.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/js/CBjquery/Cuejqzoom.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/webandpeople/custommenu/custommenu.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/js/jquery-1.8.2.min.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/bxslider/js/jquery.easing.1.3.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/js/script.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/ajaxcart/js/fancybox/jquery.fancybox-1.3.4.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/ajaxcart/js/fancybox/noconflict.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/ajaxcart/js/ajaxcart.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/cloud-zoom/js/cloud-zoom.1.0.2.min.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/bxslider/js/jquery.bxslider.min.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/bxslider/js/slider-config.js"></script>
<!--[if lt IE 8]>
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/css/styles-ie.css" media="all" />
<![endif]-->
<!--[if lt IE 7]>
<script type="text/javascript" src="https://www.imobshop.sg/js/lib/ds-sleight.js"></script>
<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/base/default/js/ie6.js"></script>
<![endif]-->
<!--[if lt IE 9]>
<link rel="stylesheet" type="text/css" href="https://www.imobshop.sg/skin/frontend/default/metrostore/css/ie-8.css" media="all" />
<![endif]-->

<script type="text/javascript">
//<![CDATA[
Mage.Cookies.path     = '/';
Mage.Cookies.domain   = '.www.imobshop.sg';
//]]>
</script>

<script type="text/javascript">
//<![CDATA[
optionalZipCountries = ["HK"];
//]]>
</script>
<!-- BEGIN GOOGLE ANALYTICS CODEs -->
<script type="text/javascript">
//<![CDATA[
    var _gaq = _gaq || [];

_gaq.push(['_setAccount', 'UA-51809241-1']);
_gaq.push (['_gat._anonymizeIp']);
_gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();

//]]>
</script>
<!-- END GOOGLE ANALYTICS CODE -->
<script type="text/javascript">//<![CDATA[
        var Translator = new Translate([]);
        //]]></script>
<link rel="stylesheet" href="https://www.imobshop.sg/skin/frontend/default/hellowired/css/mobile.css" type="text/css" />

<script>
	function successMessage(message,message1,message2)
		{
		    jQuery('body').append('<div class="alert"></div>');
		    var $alert = jQuery('.alert');
		    $alert.fadeIn(400);
		    $alert.html(message).append('<button class="close"></button>');
		    $alert.html(message1).append('<a class="close cart" href="https://www.imobshop.sg/checkout/cart/">GO TO CART</a>');
		    $alert.html(message2).append('<a class="close continue">CONTINUE SHOPPING</a>');
		    jQuery('.close').click(function () {
			$alert.fadeOut(400);
		    });
		    $alert.fadeIn('400', function () {
			setTimeout(function () {
			    $alert.fadeOut('400', function () {
				jQuery(this).fadeOut(400, function(){ jQuery(this).detach(); })
			    });
			}, 10000)
		    });
		}
</script>














<link href='https://www.imobshop.sg/skin/frontend/default/metrostore/css/themeoption.css.php?store=default' rel='stylesheet' type='text/css'>

<!--[if lt IE 9]>
	<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/ie/css3-mediaqueries.js"></script>
	<script type="text/javascript" src="https://www.imobshop.sg/skin/frontend/default/metrostore/ie/respond.min.js"></script>


<![endif]-->

</head>
<body class=" catalog-product-view catalog-product-view product-mistral-power-3x6inch-fan categorypath-home category-home">
<div class="wrapper">
        <noscript>
        <div class="global-site-notice noscript">
            <div class="notice-inner">
                <p>
                    <strong>JavaScript seems to be disabled in your browser.</strong><br />
                    You must have JavaScript enabled in your browser to utilize the functionality of this website.                </p>
            </div>
        </div>
    </noscript>
    <div class="page">
        		<div class="header-container">
    <div class="header">
     <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0,user-scalable=yes" />
	<div class="quick-access">
	    <div class="header1">


<div id="fb-root"></div>

<ul class="links">
                        <li class="first" ><a href="https://www.imobshop.sg/customer/account/" title="My Account" >My Account</a></li>
                                <li ><a href="https://www.imobshop.sg/wishlist/" title="My Wishlist" >My Wishlist</a></li>
                                <li ><a href="https://www.imobshop.sg/checkout/cart/" title="My Cart" class="top-link-cart">My Cart</a></li>
                                <li ><a href="https://www.imobshop.sg/customer/account/login/referer/aHR0cHM6Ly93d3cuaW1vYnNob3Auc2cvaG9tZS9taXN0cmFsLXBvd2VyLTN4NmluY2gtZmFuP19fX1NJRD1V/" title="Log In" >Log In</a></li>
                                <li class=" last" ><a href="https://www.imobshop.sg/customer/account/create/" title="Register" >Register</a></li>
            </ul>


            <!--<p class="welcome-msg">Welcome to iMOB Shop! </p>-->
            </div>
        </div>

        <div class="header2">
	    <a href="https://www.imobshop.sg/" title="Welcome to iMOB Shop!" class="logo"><strong>Welcome to iMOB Shop!</strong><img src="https://www.imobshop.sg/skin/frontend/default/metrostore/images/logo.png" alt="Welcome to iMOB Shop!" /></a>


          <div class="searchlogo">
                <div class="facebook">
		<div class="fb-like" data-href="https://www.facebook.com/iMOBsg" data-layout="button_count" data-action="like" data-show-faces="false" data-share="false"></div>
</div>
</div>
	    <div class="searchlogo">

<form id="search_mini_form" action="https://www.imobshop.sg/catalogsearch/result/" method="get">

    <div class="form-search">
        <label for="search">Search:</label>
        <input id="search" type="text" name="q" value="" class="input-text" maxlength="128" />
        <button type="submit" title="Search" class="button"><span><span></span></span></button>
        <div id="search_autocomplete" class="search-autocomplete"></div>
        <script type="text/javascript">
        //<![CDATA[
            var searchForm = new Varien.searchForm('search_mini_form', 'search', 'Enter your Keyword');
            searchForm.initAutocomplete('https://www.imobshop.sg/catalogsearch/ajax/suggest/', 'search_autocomplete');
        //]]>
        </script>
    </div>
</form>

</div>





	</div>

 <div class="menuwithlogo">
		<div class="menu-fix">
		<div class="nav-container">
	<div class="header2">
		<div id="custommenu" class="">
		  <!--  			<div class="menu">
				<div class="parentMenu menu0">
					<a href="https://www.imobshop.sg/">
						<span>Home</span>
					</a>
				</div>
			</div>
			-->
							<div id="menu46" class="menu parent" onmouseover="wpShowMenuPopup(this, event, 'popup46');" onmouseout="wpHideMenuPopup(this, event, 'popup46', 'menu46')">
<div class="parentMenu">
<a href="javascript:void(0);" rel="https://www.imobshop.sg/fun">
<span class="errow"></span><span>Fun</span>
</a>
</div>
</div>
<div id="popup46" class="wp-custom-menu-popup" onmouseout="wpHideMenuPopup(this, event, 'popup46', 'menu46')" onmouseover="wpPopupOver(this, event, 'popup46', 'menu46')">
<div class="block1">
<div class="column first odd"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/fun/indoor"><span>Indoor</span></a></div></div><div class="column last even"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/fun/outdoor"><span>Outdoor</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>							<div id="menu13" class="menu parent" onmouseover="wpShowMenuPopup(this, event, 'popup13');" onmouseout="wpHideMenuPopup(this, event, 'popup13', 'menu13')">
<div class="parentMenu">
<a href="javascript:void(0);" rel="https://www.imobshop.sg/tech">
<span class="errow"></span><span>Tech</span>
</a>
</div>
</div>
<div id="popup13" class="wp-custom-menu-popup" onmouseout="wpHideMenuPopup(this, event, 'popup13', 'menu13')" onmouseover="wpPopupOver(this, event, 'popup13', 'menu13')">
<div class="block1">
<div class="column first odd"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/tech/computer-accessories"><span>Computer &amp; Accessories</span></a></div></div><div class="column even"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/tech/camera-accessories"><span>Camera &amp; Accessories</span></a></div></div><div class="column last odd"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/tech/mobile-accessories"><span>Mobile &amp; Accessories</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>							<div id="menu47" class="menu parent" onmouseover="wpShowMenuPopup(this, event, 'popup47');" onmouseout="wpHideMenuPopup(this, event, 'popup47', 'menu47')">
<div class="parentMenu">
<a href="javascript:void(0);" rel="https://www.imobshop.sg/wellness">
<span class="errow"></span><span> Wellness</span>
</a>
</div>
</div>
<div id="popup47" class="wp-custom-menu-popup" onmouseout="wpHideMenuPopup(this, event, 'popup47', 'menu47')" onmouseover="wpPopupOver(this, event, 'popup47', 'menu47')">
<div class="block1">
<div class="column first odd"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/skin-care"><span>Skin Care</span></a><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/cosmetics"><span>Cosmetics</span></a></div></div><div class="column last even"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/accessories"><span>Accessories</span></a><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/beauty-services"><span>Beauty Services</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>							<div id="menu35" class="menu">
<div class="parentMenu">
<a href="https://www.imobshop.sg/food">
<span class="errow"></span><span> Food</span>
</a>
</div>
</div>							<div id="menu37" class="menu parent" onmouseover="wpShowMenuPopup(this, event, 'popup37');" onmouseout="wpHideMenuPopup(this, event, 'popup37', 'menu37')">
<div class="parentMenu">
<a href="javascript:void(0);" rel="https://www.imobshop.sg/travel">
<span class="errow"></span><span>Travel</span>
</a>
</div>
</div>
<div id="popup37" class="wp-custom-menu-popup" onmouseout="wpHideMenuPopup(this, event, 'popup37', 'menu37')" onmouseover="wpPopupOver(this, event, 'popup37', 'menu37')">
<div class="block1">
<div class="column first odd"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/travel/tickets"><span>Tickets</span></a></div></div><div class="column last even"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/travel/travelaccessories"><span>Travel Accessories</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>							<div id="menu10" class="menu parent act" onmouseover="wpShowMenuPopup(this, event, 'popup10');" onmouseout="wpHideMenuPopup(this, event, 'popup10', 'menu10')">
<div class="parentMenu">
<a href="javascript:void(0);" rel="https://www.imobshop.sg/home">
<span class="errow"></span><span>Home</span>
</a>
</div>
</div>
<div id="popup10" class="wp-custom-menu-popup" onmouseout="wpHideMenuPopup(this, event, 'popup10', 'menu10')" onmouseover="wpPopupOver(this, event, 'popup10', 'menu10')">
<div class="block1">
<div class="column first odd"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/home/appliances"><span>Appliances </span></a></div></div><div class="column last even"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/home/household"><span>Household</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>							<div id="menu45" class="menu">
<div class="parentMenu">
<a href="https://www.imobshop.sg/family">
<span class="errow"></span><span> Family</span>
</a>
</div>
</div>							<div id="menu18" class="menu parent" onmouseover="wpShowMenuPopup(this, event, 'popup18');" onmouseout="wpHideMenuPopup(this, event, 'popup18', 'menu18')">
<div class="parentMenu">
<a href="javascript:void(0);" rel="https://www.imobshop.sg/fashion">
<span class="errow"></span><span>Fashion</span>
</a>
</div>
</div>
<div id="popup18" class="wp-custom-menu-popup" onmouseout="wpHideMenuPopup(this, event, 'popup18', 'menu18')" onmouseover="wpPopupOver(this, event, 'popup18', 'menu18')">
<div class="block1">
<div class="column first odd"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/watches"><span>Watches</span></a><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/bags-and-wallets"><span>Bags and Wallets</span></a></div></div><div class="column last even"><div class="itemMenu level1"><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/ladies"><span>Ladies'</span></a><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/men-s"><span>Men's</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>							<div id="menu168" class="menu">
<div class="parentMenu">
<a href="https://www.imobshop.sg/shop">
<span class="errow"></span><span>Shop</span>
</a>
</div>
</div>						<div class="clearBoth"></div>
		</div>
	</div>

    <div id="custommenu-mobile" class="" style="display:none;">
        <div id="menu-button" onclick="wpMenuButtonToggle()">
            <a href="javascript:void(0);">
                <span>Menu</span>
            </a>
        </div>
        <div id="menu-content" style="display:none;">
                        <div id="menu-mobile-0" class="menu-mobile level0">
                <div class="parentMenu">
                    <a href="https://www.imobshop.sg/">
                        <span>Home</span>
                    </a>
                </div>
            </div>
                                        <div id="menu-mobile-46" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/fun">
<span>Fun</span>
</a>
<span class="button" rel="submenu-mobile-46" onclick="wpSubMenuToggle(this, 'menu-mobile-46', 'submenu-mobile-46');">&nbsp</span>
</div>
<div id="submenu-mobile-46" rel="level0" class="wp-custom-menu-submenu" style="display: none;">
<div id="menu-mobile-155" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/fun/indoor"><span>Indoor</span></a></div></div><div id="menu-mobile-156" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/fun/outdoor"><span>Outdoor</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>                            <div id="menu-mobile-13" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/tech">
<span>Tech</span>
</a>
<span class="button" rel="submenu-mobile-13" onclick="wpSubMenuToggle(this, 'menu-mobile-13', 'submenu-mobile-13');">&nbsp</span>
</div>
<div id="submenu-mobile-13" rel="level0" class="wp-custom-menu-submenu" style="display: none;">
<div id="menu-mobile-147" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/tech/computer-accessories"><span>Computer &amp; Accessories</span></a></div></div><div id="menu-mobile-148" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/tech/camera-accessories"><span>Camera &amp; Accessories</span></a></div></div><div id="menu-mobile-158" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/tech/mobile-accessories"><span>Mobile &amp; Accessories</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>                            <div id="menu-mobile-47" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/wellness">
<span> Wellness</span>
</a>
<span class="button" rel="submenu-mobile-47" onclick="wpSubMenuToggle(this, 'menu-mobile-47', 'submenu-mobile-47');">&nbsp</span>
</div>
<div id="submenu-mobile-47" rel="level0" class="wp-custom-menu-submenu" style="display: none;">
<div id="menu-mobile-159" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/skin-care"><span>Skin Care</span></a></div></div><div id="menu-mobile-160" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/cosmetics"><span>Cosmetics</span></a></div></div><div id="menu-mobile-161" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/accessories"><span>Accessories</span></a></div></div><div id="menu-mobile-162" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/wellness/beauty-services"><span>Beauty Services</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>                            <div id="menu-mobile-35" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/food">
<span> Food</span>
</a>
</div>
</div>                            <div id="menu-mobile-37" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/travel">
<span>Travel</span>
</a>
<span class="button" rel="submenu-mobile-37" onclick="wpSubMenuToggle(this, 'menu-mobile-37', 'submenu-mobile-37');">&nbsp</span>
</div>
<div id="submenu-mobile-37" rel="level0" class="wp-custom-menu-submenu" style="display: none;">
<div id="menu-mobile-149" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/travel/tickets"><span>Tickets</span></a></div></div><div id="menu-mobile-150" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/travel/travelaccessories"><span>Travel Accessories</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>                            <div id="menu-mobile-10" class="menu-mobile level0 act">
<div class="parentMenu">
<a href="https://www.imobshop.sg/home">
<span>Home</span>
</a>
<span class="button" rel="submenu-mobile-10" onclick="wpSubMenuToggle(this, 'menu-mobile-10', 'submenu-mobile-10');">&nbsp</span>
</div>
<div id="submenu-mobile-10" rel="level0" class="wp-custom-menu-submenu" style="display: none;">
<div id="menu-mobile-151" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/home/appliances"><span>Appliances </span></a></div></div><div id="menu-mobile-152" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/home/household"><span>Household</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>                            <div id="menu-mobile-45" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/family">
<span> Family</span>
</a>
</div>
</div>                            <div id="menu-mobile-18" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/fashion">
<span>Fashion</span>
</a>
<span class="button" rel="submenu-mobile-18" onclick="wpSubMenuToggle(this, 'menu-mobile-18', 'submenu-mobile-18');">&nbsp</span>
</div>
<div id="submenu-mobile-18" rel="level0" class="wp-custom-menu-submenu" style="display: none;">
<div id="menu-mobile-153" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/watches"><span>Watches</span></a></div></div><div id="menu-mobile-154" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/bags-and-wallets"><span>Bags and Wallets</span></a></div></div><div id="menu-mobile-164" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/ladies"><span>Ladies'</span></a></div></div><div id="menu-mobile-165" class="itemMenu level1"><div class="parentMenu"><a class="itemMenuName level1" href="https://www.imobshop.sg/fashion/men-s"><span>Men's</span></a></div></div>
<div class="clearBoth"></div>
</div>
</div>                            <div id="menu-mobile-168" class="menu-mobile level0">
<div class="parentMenu">
<a href="https://www.imobshop.sg/shop">
<span>Shop</span>
</a>
</div>
</div>                        <div class="clearBoth"></div>
        </div>
    </div>
</div>
<script type="text/javascript">
//<![CDATA[
var CUSTOMMENU_POPUP_WIDTH = 0;
var CUSTOMMENU_POPUP_TOP_OFFSET = 0;
var CUSTOMMENU_POPUP_DELAY_BEFORE_DISPLAYING = 0;
var CUSTOMMENU_POPUP_DELAY_BEFORE_HIDING = 0;
var CUSTOMMENU_RTL_MODE = 0;
var wpCustommenuTimerShow = {};
var wpCustommenuTimerHide = {};
var wpActiveMenu = null;
wpCustomMenuMobileToggle();
//]]>
</script>
		<div class="shopping_bg">
			<div class="cartlogo"></div>
			<!--<h1>Shopping Bag</h1>-->

					</div>
		</div>
	    </div>


            </div>
</div>
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=642939932422937&version=v2.0";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

        <div class="main-container col1-layout">
            <div class="main">
                                <div class="breadcrumbs">
    <ul>
                    <li class="home">
                            <a href="https://www.imobshop.sg/" title="Go to Home Page">Home</a>
                                        <span></span>
                        </li>
                    <li class="category10">
                            <a href="https://www.imobshop.sg/home" title="">Home</a>
                                        <span></span>
                        </li>
                    <li class="product">
                            <strong>Mistral Power 3x6inch Fan</strong>
                                    </li>
            </ul>
</div>


                <div class="col-main">
                                        <script type="text/javascript">
    var optionsPrice = new Product.OptionsPrice({"productId":"879","priceFormat":{"pattern":"S$%s","precision":2,"requiredPrecision":2,"decimalSymbol":".","groupSymbol":",","groupLength":3,"integerRequired":1},"includeTax":"false","showIncludeTax":false,"showBothPrices":false,"productPrice":85,"productOldPrice":129,"priceInclTax":85,"priceExclTax":85,"skipCalculate":1,"defaultTax":0,"currentTax":0,"idSuffix":"_clone","oldPlusDisposition":0,"plusDisposition":0,"plusDispositionTax":0,"oldMinusDisposition":0,"minusDisposition":0,"tierPrices":[],"tierPricesInclTax":[]});
</script>
<div id="messages_product_view"></div>




<div class="product-view">
    <div class="product-essential">
    <form action="https://www.imobshop.sg/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuaW1vYnNob3Auc2cvaG9tZS9taXN0cmFsLXBvd2VyLTN4NmluY2gtZmFuP19fX1NJRD1V/product/879/form_key/sfYWSzfY3JHPSmHd/" method="post" id="product_addtocart_form" enctype="multipart/form-data">
        <div class="no-display">
            <input type="hidden" name="product" value="879" />
            <input type="hidden" name="related_product" id="related-products-field" value="" />
        </div>

        <div class="default-image product-img-box">



    <p class="product-image product-image-zoom">
	<a rel="zoomWidth: '350',zoomHeight: '350',position: 'inside',smoothMove: 3,showTitle: true,titleOpacity: 0,lensOpacity: 0,tintOpacity: 0,softFocus: false" gallery="https://www.imobshop.sg/catalog/product/gallery/id/879/image/3998/" href="https://www.imobshop.sg/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/c/o/cover_image_21_6.jpg" class="cloud-zoom" id="cloudZoom">
	<img id="image" src="https://www.imobshop.sg/media/catalog/product/cache/1/image/350x350/9df78eab33525d08d6e5fb8d27136e95/c/o/cover_image_21_6.jpg" alt="Mistral Power 3x6inch Fan" title="Mistral Power 3x6inch Fan" />	</a>
    </p>

    <div class="default-views more-views">
	<ul class="slider6"><li><a href="https://www.imobshop.sg/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/c/o/cover_image_21_6.jpg" rel="popupWin:'https://www.imobshop.sg/catalog/product/gallery/id/879/image/3998/', useZoom: 'cloudZoom', smallImage: 'https://www.imobshop.sg/media/catalog/product/cache/1/image/350x350/9df78eab33525d08d6e5fb8d27136e95/c/o/cover_image_21_6.jpg'" class="cloud-zoom-gallery" title=""><img src="https://www.imobshop.sg/media/catalog/product/cache/1/thumbnail/84x77/9df78eab33525d08d6e5fb8d27136e95/c/o/cover_image_21_6.jpg" alt="" /></a></li><li><a href="https://www.imobshop.sg/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox2_4_2.jpg" rel="popupWin:'https://www.imobshop.sg/catalog/product/gallery/id/879/image/3997/', useZoom: 'cloudZoom', smallImage: 'https://www.imobshop.sg/media/catalog/product/cache/1/image/350x350/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox2_4_2.jpg'" class="cloud-zoom-gallery" title=""><img src="https://www.imobshop.sg/media/catalog/product/cache/1/thumbnail/84x77/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox2_4_2.jpg" alt="" /></a></li><li><a href="https://www.imobshop.sg/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox3_4.jpg" rel="popupWin:'https://www.imobshop.sg/catalog/product/gallery/id/879/image/3996/', useZoom: 'cloudZoom', smallImage: 'https://www.imobshop.sg/media/catalog/product/cache/1/image/350x350/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox3_4.jpg'" class="cloud-zoom-gallery" title=""><img src="https://www.imobshop.sg/media/catalog/product/cache/1/thumbnail/84x77/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox3_4.jpg" alt="" /></a></li><li><a href="https://www.imobshop.sg/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox1_5_2.jpg" rel="popupWin:'https://www.imobshop.sg/catalog/product/gallery/id/879/image/3995/', useZoom: 'cloudZoom', smallImage: 'https://www.imobshop.sg/media/catalog/product/cache/1/image/350x350/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox1_5_2.jpg'" class="cloud-zoom-gallery" title=""><img src="https://www.imobshop.sg/media/catalog/product/cache/1/thumbnail/84x77/9df78eab33525d08d6e5fb8d27136e95/i/m/imagebox1_5_2.jpg" alt="" /></a></li></ul>    </div>
        </div>

        <div class="default-shop product-shop">
            <div class="view-name">
                <div class="product-name">
                        <h1>Mistral Power 3x6inch Fan</h1>
                </div>
            </div>

                            <p class="email-friend"><a href="https://www.imobshop.sg/sendfriend/product/send/id/879/cat_id/10/">Email to a Friend</a></p>

                <p class="no-rating"><a onclick="doShowReviewform('product_tabs_addreviews')" href="#product_tabs_addreviews">Be the first to review this product</a></p>
                        <div class="price-stock">



    <div class="price-box">

                    <p class="old-price">
                <span class="price-label">Regular Price:</span>
                <span class="price" id="old-price-879">
                    S$129.00                </span>
            </p>

                            <p class="special-price">
                    <span class="price-label">Special Price</span>
                <span class="price" id="product-price-879">
                    S$85.00                </span>
                </p>


        </div>


                    <p class="availability in-stock"> <span>In stock</span></p>
                </div>

            <div style="clear: both;"></div>
<div  class="linker_seller">
    </div>

	    <div class="sku-brand">
		<div class="product_sku" style="display:none">
		    <label>SKU :</label>
		    IM617		</div>

			    </div>

                            <div class="short-description">
                    <h2>Quick Overview</h2>
                    <div class="std"><p>Mistral Power Fan 3x6inch Fan (MDC306GW)<br />3x6inch Fan Blades<br />Wide angle 235 degree oscillation<br />Energy Saving DC Motor (saves up to 60%)<br />3 Year Motor Warranty</p><br />
<p>Remarks: Choice of Seller Delivery <strong>OR</strong> Self Collection at Holland Village, Sembawang, East Coast Road, Bedok North</p></div>
                </div>






                        <div class="product-options" id="product-options-wrapper">
    <script type="text/javascript">
//<![CDATA[
var DateOption = Class.create({

    getDaysInMonth: function(month, year)
    {
        var curDate = new Date();
        if (!month) {
            month = curDate.getMonth();
        }
        if (2 == month && !year) { // leap year assumption for unknown year
            return 29;
        }
        if (!year) {
            year = curDate.getFullYear();
        }
        return 32 - new Date(year, month - 1, 32).getDate();
    },

    reloadMonth: function(event)
    {
        var selectEl = event.findElement();
        var idParts = selectEl.id.split("_");
        if (idParts.length != 3) {
            return false;
        }
        var optionIdPrefix = idParts[0] + "_" + idParts[1];
        var month = parseInt($(optionIdPrefix + "_month").value);
        var year = parseInt($(optionIdPrefix + "_year").value);
        var dayEl = $(optionIdPrefix + "_day");

        var days = this.getDaysInMonth(month, year);

        //remove days
        for (var i = dayEl.options.length - 1; i >= 0; i--) {
            if (dayEl.options[i].value > days) {
                dayEl.remove(dayEl.options[i].index);
            }
        }

        // add days
        var lastDay = parseInt(dayEl.options[dayEl.options.length-1].value);
        for (i = lastDay + 1; i <= days; i++) {
            this.addOption(dayEl, i, i);
        }
    },

    addOption: function(select, text, value)
    {
        var option = document.createElement('OPTION');
        option.value = value;
        option.text = text;

        if (select.options.add) {
            select.options.add(option);
        } else {
            select.appendChild(option);
        }
    }
});
dateOption = new DateOption();
//]]>
</script>

    <script type="text/javascript">
    //<![CDATA[
    var optionFileUpload = {
        productForm : $('product_addtocart_form'),
        formAction : '',
        formElements : {},
        upload : function(element){
            this.formElements = this.productForm.select('input', 'select', 'textarea', 'button');
            this.removeRequire(element.readAttribute('id').sub('option_', ''));

            template = '<iframe id="upload_target" name="upload_target" style="width:0; height:0; border:0;"><\/iframe>';

            Element.insert($('option_'+element.readAttribute('id').sub('option_', '')+'_uploaded_file'), {after: template});

            this.formAction = this.productForm.action;

            var baseUrl = 'https://www.imobshop.sg/catalog/product/upload/';
            var urlExt = 'option_id/'+element.readAttribute('id').sub('option_', '');

            this.productForm.action = parseSidUrl(baseUrl, urlExt);
            this.productForm.target = 'upload_target';
            this.productForm.submit();
            this.productForm.target = '';
            this.productForm.action = this.formAction;
        },
        removeRequire : function(skipElementId){
            for(var i=0; i<this.formElements.length; i++){
                if (this.formElements[i].readAttribute('id') != 'option_'+skipElementId+'_file' && this.formElements[i].type != 'button') {
                    this.formElements[i].disabled='disabled';
                }
            }
        },
        addRequire : function(skipElementId){
            for(var i=0; i<this.formElements.length; i++){
                if (this.formElements[i].readAttribute('name') != 'options_'+skipElementId+'_file' && this.formElements[i].type != 'button') {
                    this.formElements[i].disabled='';
                }
            }
        },
        uploadCallback : function(data){
            this.addRequire(data.optionId);
            $('upload_target').remove();

            if (data.error) {

            } else {
                $('option_'+data.optionId+'_uploaded_file').value = data.fileName;
                $('option_'+data.optionId+'_file').value = '';
                $('option_'+data.optionId+'_file').hide();
                $('option_'+data.optionId+'').hide();
                template = '<div id="option_'+data.optionId+'_file_box"><a href="#"><img src="var/options/'+data.fileName+'" alt=""><\/a><a href="#" onclick="optionFileUpload.removeFile('+data.optionId+')" title="Remove file" \/>Remove file<\/a>';

                Element.insert($('option_'+data.optionId+'_uploaded_file'), {after: template});
            }
        },
        removeFile : function(optionId)
        {
            $('option_'+optionId+'_uploaded_file').value= '';
            $('option_'+optionId+'_file').show();
            $('option_'+optionId+'').show();

            $('option_'+optionId+'_file_box').remove();
        }
    }
    var optionTextCounter = {
        count : function(field,cntfield,maxlimit){
            if (field.value.length > maxlimit){
                field.value = field.value.substring(0, maxlimit);
            } else {
                cntfield.innerHTML = maxlimit - field.value.length;
            }
        }
    }

    Product.Options = Class.create();
    Product.Options.prototype = {
        initialize : function(config) {
            this.config = config;
            this.reloadPrice();
            document.observe("dom:loaded", this.reloadPrice.bind(this));
        },
        reloadPrice : function() {
            var config = this.config;
            var skipIds = [];
            $$('body .product-custom-option').each(function(element){
                var optionId = 0;
                element.name.sub(/[0-9]+/, function(match){
                    optionId = parseInt(match[0], 10);
                });
                if (config[optionId]) {
                    var configOptions = config[optionId];
                    var curConfig = {price: 0};
                    if (element.type == 'checkbox' || element.type == 'radio') {
                        if (element.checked) {
                            if (typeof configOptions[element.getValue()] != 'undefined') {
                                curConfig = configOptions[element.getValue()];
                            }
                        }
                    } else if(element.hasClassName('datetime-picker') && !skipIds.include(optionId)) {
                        dateSelected = true;
                        $$('.product-custom-option[id^="options_' + optionId + '"]').each(function(dt){
                            if (dt.getValue() == '') {
                                dateSelected = false;
                            }
                        });
                        if (dateSelected) {
                            curConfig = configOptions;
                            skipIds[optionId] = optionId;
                        }
                    } else if(element.type == 'select-one' || element.type == 'select-multiple') {
                        if ('options' in element) {
                            $A(element.options).each(function(selectOption){
                                if ('selected' in selectOption && selectOption.selected) {
                                    if (typeof(configOptions[selectOption.value]) != 'undefined') {
                                        curConfig = configOptions[selectOption.value];
                                    }
                                }
                            });
                        }
                    } else {
                        if (element.getValue().strip() != '') {
                            curConfig = configOptions;
                        }
                    }
                    if(element.type == 'select-multiple' && ('options' in element)) {
                        $A(element.options).each(function(selectOption) {
                            if (('selected' in selectOption) && typeof(configOptions[selectOption.value]) != 'undefined') {
                                if (selectOption.selected) {
                                    curConfig = configOptions[selectOption.value];
                                } else {
                                    curConfig = {price: 0};
                                }
                                optionsPrice.addCustomPrices(optionId + '-' + selectOption.value, curConfig);
                                optionsPrice.reload();
                            }
                        });
                    } else {
                        optionsPrice.addCustomPrices(element.id || optionId, curConfig);
                        optionsPrice.reload();
                    }
                }
            });
        }
    }
    function validateOptionsCallback(elmId, result) {
        var container = $(elmId).up('ul.options-list');
        if (result == 'failed') {
            container.removeClassName('validation-passed');
            container.addClassName('validation-failed');
        } else {
            container.removeClassName('validation-failed');
            container.addClassName('validation-passed');
        }
    }
    var opConfig = new Product.Options({"468":{"2035":{"price":8.9,"oldPrice":8.9,"priceValue":"8.9000","type":"fixed","excludeTax":8.9,"includeTax":8.9},"2036":{"price":0,"oldPrice":0,"priceValue":"0.0000","type":"fixed","excludeTax":0,"includeTax":0},"2037":{"price":0,"oldPrice":0,"priceValue":"0.0000","type":"fixed","excludeTax":0,"includeTax":0},"2038":{"price":0,"oldPrice":0,"priceValue":"0.0000","type":"fixed","excludeTax":0,"includeTax":0},"2039":{"price":0,"oldPrice":0,"priceValue":"0.0000","type":"fixed","excludeTax":0,"includeTax":0}}});
    //]]>
    </script>
    <dl>

<dt><label class="required"><em>*</em>Delivery Option</label></dt>
<dd class="last">
    <div class="input-box">
        <select name="options[468]" id="select_468" class=" required-entry product-custom-option" title=""  onchange="opConfig.reloadPrice()"><option value="" >-- Please Select --</option><option value="2035"  price="8.9" >Seller Delivery +S$8.90</option><option value="2036"  price="0" >Self Collection at Holland Village </option><option value="2037"  price="0" >Self Collection at Sembawang </option><option value="2038"  price="0" >Self Collection at East Coast Road </option><option value="2039"  price="0" >Self Collection at Bedok North </option></select>                                </div>
</dd>
        </dl>

<script type="text/javascript">
//<![CDATA[
enUS = {"m":{"wide":["January","February","March","April","May","June","July","August","September","October","November","December"],"abbr":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]}}; // en_US locale reference
Calendar._DN = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]; // full day names
Calendar._SDN = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]; // short day names
Calendar._FD = 1; // First day of the week. "0" means display Sunday first, "1" means display Monday first, etc.
Calendar._MN = ["January","February","March","April","May","June","July","August","September","October","November","December"]; // full month names
Calendar._SMN = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]; // short month names
Calendar._am = "AM"; // am/pm
Calendar._pm = "PM";

// tooltips
Calendar._TT = {};
Calendar._TT["INFO"] = "About the calendar";

Calendar._TT["ABOUT"] =
"DHTML Date/Time Selector\n" +
"(c) dynarch.com 2002-2005 / Author: Mihai Bazon\n" +
"For latest version visit: http://www.dynarch.com/projects/calendar/\n" +
"Distributed under GNU LGPL. See http://gnu.org/licenses/lgpl.html for details." +
"\n\n" +
"Date selection:\n" +
"- Use the \xab, \xbb buttons to select year\n" +
"- Use the " + String.fromCharCode(0x2039) + ", " + String.fromCharCode(0x203a) + " buttons to select month\n" +
"- Hold mouse button on any of the above buttons for faster selection.";
Calendar._TT["ABOUT_TIME"] = "\n\n" +
"Time selection:\n" +
"- Click on any of the time parts to increase it\n" +
"- or Shift-click to decrease it\n" +
"- or click and drag for faster selection.";

Calendar._TT["PREV_YEAR"] = "Prev. year (hold for menu)";
Calendar._TT["PREV_MONTH"] = "Prev. month (hold for menu)";
Calendar._TT["GO_TODAY"] = "Go Today";
Calendar._TT["NEXT_MONTH"] = "Next month (hold for menu)";
Calendar._TT["NEXT_YEAR"] = "Next year (hold for menu)";
Calendar._TT["SEL_DATE"] = "Select date";
Calendar._TT["DRAG_TO_MOVE"] = "Drag to move";
Calendar._TT["PART_TODAY"] = ' (' + "Today" + ')';

// the following is to inform that "%s" is to be the first day of week
Calendar._TT["DAY_FIRST"] = "Display %s first";

// This may be locale-dependent. It specifies the week-end days, as an array
// of comma-separated numbers. The numbers are from 0 to 6: 0 means Sunday, 1
// means Monday, etc.
Calendar._TT["WEEKEND"] = "0,6";

Calendar._TT["CLOSE"] = "Close";
Calendar._TT["TODAY"] = "Today";
Calendar._TT["TIME_PART"] = "(Shift-)Click or drag to change value";

// date formats
Calendar._TT["DEF_DATE_FORMAT"] = "%b %e, %Y";
Calendar._TT["TT_DATE_FORMAT"] = "%B %e, %Y";

Calendar._TT["WK"] = "Week";
Calendar._TT["TIME"] = "Time:";
//]]>
</script>
            <p class="required">* Required Fields</p>
    </div>
<script type="text/javascript">decorateGeneric($$('#product-options-wrapper dl'), ['last']);</script>
<div class="product-options-bottom">



    <div class="price-box">

                    <p class="old-price">
                <span class="price-label">Regular Price:</span>
                <span class="price" id="old-price-879_clone">
                    S$129.00                </span>
            </p>

                            <p class="special-price">
                    <span class="price-label">Special Price</span>
                <span class="price" id="product-price-879_clone">
                    S$85.00                </span>
                </p>


        </div>



<script type="text/javascript">
//<![CDATA[

    var json_tier_prices = [];

    function getTierPriceCorrection(qty, default_points){
        //j2t_math_points
        var return_value = default_points;
        if(json_tier_prices.length > 0){
            for (var k=0; k < json_tier_prices.length; k++) {
                if (qty >= json_tier_prices[k]['price_qty']){
                    return_value = json_tier_prices[k]['productTierPoints'];
                }
            }
        }
        return return_value;
    }

    function checkJ2tPoints(){
        var points = $('j2t-pts').innerHTML;
        if (points > 0){
            $$('.j2t-loyalty-points').invoke('show');
        } else {
            $$('.j2t-loyalty-points').invoke('hide');
        }
        modifyJ2tEquivalence($('j2t-pts').innerHTML);
        checkJ2tCloneText();
    }

    function checkJ2tCloneText(){
        if ($('j2t-points-clone') && $$(".j2t-loyalty-points").length > 0){
            $('j2t-points-clone').style.display = $$(".j2t-loyalty-points")[0].style.display;
            var text_clone = $$(".j2t-loyalty-points")[0].innerHTML;
            text_clone = text_clone.replace("j2t-pts", "j2t-pts-clone");
            text_clone = text_clone.replace("j2t-point-equivalence", "j2t-point-equivalence-clone");
            $('j2t-points-clone').innerHTML = text_clone;
        }
    }

    Number.prototype.j2tFormatMoney = function(c, d, t){
        var n = this, c = isNaN(c = Math.abs(c)) ? 2 : c, d = d == undefined ? "," : d, t = t == undefined ? "." : t, s = n < 0 ? "-" : "", i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "", j = (j = i.length) > 3 ? j % 3 : 0;
        return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
    };


        var j2t_mil_sep = ",";

    var j2t_dec_sep = ".";

    var j2t_convert_template = (12345.23).j2tFormatMoney(2, j2t_dec_sep, j2t_mil_sep);

    var j2t_point_currency_base = "1";
    //var j2t_point_currency_currency = "S$1.00";
    var j2t_point_currency = "S$1.00";
    j2t_point_currency = j2t_point_currency.replace((1.00).j2tFormatMoney(2, j2t_dec_sep, j2t_mil_sep), "__MONEY__");

    var j2t_point_default_point_unit_base = "S$0.02";
    var j2t_point_default_point_unit = 0.02;
    j2t_point_default_point_unit = (j2t_point_default_point_unit) ? j2t_point_default_point_unit : 1;
    var j2t_point_equivalence_txt = "1111 points = 2222.";

    function modifyJ2tEquivalence(current_points) {

        if ($$(".j2t-point-equivalence").length > 0){

            var money_equivalence = current_points * j2t_point_default_point_unit * j2t_point_currency_base;
            money_equivalence = Math.round(money_equivalence * 100)/100;
            money_equivalence = j2t_point_currency.replace("__MONEY__", (money_equivalence).j2tFormatMoney(2, j2t_dec_sep, j2t_mil_sep));
            //alert(j2t_point_currency);
            var return_value = j2t_point_equivalence_txt.replace("1111", current_points);
            return_value = return_value.replace("2222", money_equivalence);
            $$(".j2t-point-equivalence")[0].innerHTML = return_value;
        }

    }
//]]>
</script>



<script type="text/javascript">
//<![CDATA[
    var j2t_points = 85;
    var j2t_options = 0;

    var j2t_product_id = 879;
    document.observe("dom:loaded", function() {



        if ($('qty')){
            //Event.observe($('qty'), 'keyup', function(){ if (!isNaN($('qty').value)) {$('j2t-pts').innerHTML = j2t_math_points($('qty').value, j2t_points, true); } checkJ2tPoints();});
            Event.observe($('qty'), 'keyup', function(){ processPointsSelects() });
        }

        var product_settings   = $$('.super-attribute-select');

        processPointsSelects = function () {
            if (product_settings.length > 0){
                var concat_val = '';
                j2t_points = 0;
                var dont_process_it = false;
                $$('.super-attribute-select').each(function(el){
                    if(el.value == ''){
                        dont_process_it = true;
                    }
                    if (concat_val != ''){
                        concat_val += '|'+el.value;
                    } else {
                        concat_val = el.value;
                    }
                });
                if (!dont_process_it && concat_val != ''){
                    //load points in ajax according to attributes
                    var used_qty = 0;
                    if ($('qty')){
                        used_qty = $('qty').value;
                    }
                    used_qty = (used_qty <= 0 || used_qty == "" || isNaN(used_qty)) ? 1 : used_qty;
                    if (json_credit[concat_val] != undefined){
                        j2t_points = json_credit[concat_val];
                        if (json_credit[concat_val+'|tierPrice'] != undefined){
                            var tierprices = json_credit[concat_val+'|tierPrice'];
                            if(tierprices.length > 0){
                                for (var k=0; k < tierprices.length; k++) {
                                    if (used_qty >= tierprices[k]['price_qty']){
                                        j2t_points = tierprices[k]['productTierPoints'];
                                    }
                                }
                            }
                        }
                        $('j2t-pts').innerHTML = j2t_math_points(used_qty, j2t_points, false);
                        checkJ2tPoints();
                    }
                } else {
                    //if (!isNaN($('qty').value)) {$('j2t-pts').innerHTML = j2t_math_points($('qty').value, j2t_points, true); } checkJ2tPoints();
                }
            } else {
                var test_qty = 0;
                if ($('qty')){
                    test_qty = $('qty').value;
                }
                if (!isNaN(test_qty)) {$('j2t-pts').innerHTML = j2t_math_points(test_qty, j2t_points, true); } checkJ2tPoints();
            }
        }


        if (product_settings.length > 0){
                product_settings.each(function(element){
                Event.observe(element, 'change', function() {
                    if (element.value != ''){
                        processPointsSelects();
                    }
                });
            });
            var json_credit = [];
        }

            });

    function j2t_math_points(qty, pts_changed, tierprice_verification){
        if (tierprice_verification){
            pts_changed = getTierPriceCorrection(qty, pts_changed);
        }
        var val_return = 0;
        if (isNaN(parseFloat(qty))) {
            qty = 1;
        }
        if(qty > 0){
            val_return = (pts_changed + j2t_options) * qty;
        } else if(pts_changed > 0) {
            val_return = pts_changed + j2t_options;
        }

        return Math.ceil(val_return);
    }
//]]>
</script>



<script type="text/javascript">
//<![CDATA[
    var json_option_credit = {"468":{"2035":8.9,"2036":0,"2037":0,"2038":0,"2039":0}};

    document.observe("dom:loaded", function() {
        option_select   = $$('.product-custom-option');

        if (option_select.length > 0){
            option_select.each(function(element){
                Event.observe(element, 'change', function() {
                    j2t_options = reloadCreditOption();
                    var test_qty = 0;
                    if ($('qty')){
                        test_qty = $('qty').value;
                    }
                    $('j2t-pts').innerHTML = j2t_math_points(test_qty, j2t_points, true);
                    checkJ2tPoints();
                });
            });
        }
    });



    function reloadCreditOption(){
        var optionPts = 0;





        config = json_option_credit;
        skipIds = [];
        $$('.product-custom-option').each(function(element){
            var optionId = 0;
            element.name.sub(/[0-9]+/, function(match){
                optionId = match[0];
            });
            if (config[optionId]) {
                if (element.type == 'checkbox' || element.type == 'radio') {
                    if (element.checked) {
                        if (config[optionId][element.getValue()]) {
                            optionPts += parseFloat(config[optionId][element.getValue()]);
                        }
                    }
                } else if(element.hasClassName('datetime-picker') && !skipIds.include(optionId)) {
                    dateSelected = true;
                    $$('.product-custom-option[id^="options_' + optionId + '"]').each(function(dt){
                        if (dt.getValue() == '') {
                            dateSelected = false;
                        }
                    });
                    if (dateSelected) {
                        optionPts += parseFloat(config[optionId]);
                        skipIds[optionId] = optionId;
                    }
                } else if(element.type == 'select-one' || element.type == 'select-multiple') {
                    if (element.options) {
                        $A(element.options).each(function(selectOption){
                            if (selectOption.selected) {
                                if (config[optionId][selectOption.value]) {
                                    optionPts += parseFloat(config[optionId][selectOption.value]);
                                }
                            }
                        });
                    }
                } else {
                    if (element.getValue().strip() != '') {
                        optionPts += parseFloat(config[optionId]);
                    }
                }
            }
        });


        return optionPts;
    }

    checkJ2tCloneText();


//]]>
</script>

    <div class="add-to-cart">
                <label for="qty">Quantity:</label>
        <input type="text" name="qty" id="qty" maxlength="12" value="1" title="Qty" class="input-text qty" />


    </div>
    <div class="ajax-button">
	<button type="button" title="Add to Cart" class="button btn-cart" onclick="productAddToCartForm.submit(this)"><span><span>Add to Cart</span></span></button>
	<div id='ajax_loader' class="ajaxcartpro_progress" style="display: none;">
	    <img src="https://www.imobshop.sg/skin/frontend/default/metrostore/ajaxcart/images/al.gif">
	</div>
    </div>
    <ul class="add-to-links">
	<li>
	    <a href="https://www.imobshop.sg/home/mistral-power-3x6inch-fan" target="_parent" onclick="javascript:parent.jQuery.fancybox.close();" title="" class="view-detail"><div class="tooltip">View Detail<div class="errow"></div></div></a>
	</li>
    </ul>

<ul class="add-to-links">
    <li><a href="https://www.imobshop.sg/wishlist/index/add/product/879/form_key/sfYWSzfY3JHPSmHd/" class="link-wishlist">	<div class="tooltip">Add to Wishlist<div class="errow"></div></div>

	</a></li>
    <li><span class="separator">|</span> <a href="https://www.imobshop.sg/catalog/product_compare/add/product/879/uenc/aHR0cHM6Ly93d3cuaW1vYnNob3Auc2cvaG9tZS9taXN0cmFsLXBvd2VyLTN4NmluY2gtZmFu/form_key/sfYWSzfY3JHPSmHd/" class="link-compare">	<div class="tooltip">Add to Compare<div class="errow"></div></div>
	</a></li>
</ul>
<br />
<div id="tw-tweet"></div>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
</div>







        </div>

        	    <div class="product-right">
		<div class="customized"><!--<h5 style="font-size: 13px;">What other customers are also searching for</h5>--> <!--<div class="best_theme">-->
<div> <!--
<div class="theme_image">
<img src="https://www.imobshop.sg/media/wysiwyg/category-banner/detail-block.jpg" alt="" />
</div>
<a class="button" title="best theme" href="#"><span>Click to know more</span></a></div>
--></div>
</div>	    </div>
	        <div class="clearer"></div>

    </form>
    <script type="text/javascript">
    //<![CDATA[

	var productAddToCartForm = new VarienForm('product_addtocart_form');
        productAddToCartForm.submit = function(button, url) {
            if (this.validator.validate()) {
                var form = this.form;
                var oldUrl = form.action;

                if (url) {
                   form.action = url;
                }
                var e = null;
                try {
                    this.form.submit();
                } catch (e) {
                }
                this.form.action = oldUrl;
                if (e) {
                    throw e;
                }

                if (button && button != 'undefined') {
                    button.disabled = true;
                }
            }
        }.bind(productAddToCartForm);

        productAddToCartForm.submitLight = function(button, url){
            if(this.validator) {
                var nv = Validation.methods;
                delete Validation.methods['required-entry'];
                delete Validation.methods['validate-one-required'];
                delete Validation.methods['validate-one-required-by-name'];
                // Remove custom datetime validators
                for (var methodName in Validation.methods) {
                    if (methodName.match(/^validate-datetime-.*/i)) {
                        delete Validation.methods[methodName];
                    }
                }

                if (this.validator.validate()) {
                    if (url) {
                        this.form.action = url;
                    }
                    this.form.submit();
                }
                Object.extend(Validation.methods, nv);
            }
        }.bind(productAddToCartForm);

        //]]>
    </script>
    </div>

    <div class="product-collateral">

<div class="tabs-bg">
<ul id="tabs" class="tabs">
      <li id="product_tabs_description" class="active"><a href="#"><span>Description</span></a></li>
        <li id="product_tabs_additional" ><a href="#"><span>Additional Information</span></a></li>
        <li id="product_tabs_reviews" ><a href="#"><span>Reviews</span></a></li>
        <li id="product_tabs_addreviews" ><a href="#"><span>Add Review</span></a></li>
    </ul>
</div>

<div class="clearall"></div>
<div id="content">
	<div class="padder">
	  	  	  <div id="product_tabs_description_contents" class="prouct_tabs">    <h2>Details</h2>
    <div class="std">
        <p><span style="text-decoration: underline; font-size: small;"><strong>Terms and Conditions</strong></span><br /><br />Return Policy:<br /><span>Voucher is valid within 2 months upon purchase.</span><br />We offer 1 for 1 exchange for items with manufacturing defect. Please contact us within 7 days for an exchange at&nbsp;<a href="mailto:onlinesales@parisilk.com">onlinesales@parisilk.com</a>&nbsp;or&nbsp;64712329.</p>
<p><strong><span style="text-decoration: underline;"><span style="font-size: small;">Redemption Details</span><br /><br /></span></strong><strong>For Self-Collection: </strong></p>
<p>Redemption Details<br />&bull; For self-collection, reservation is strictly required; please call 64712329 and quote "iMOB" at least 1 day in advance before coming down to redeem your product<br />&bull; Please refer below for redemption locations<br />&bull; Timing: 11am to 7.30pm (Mon - Sat)<br />&bull; <strong>Printed voucher must be presented upon redemption<br /></strong>&bull; Buyers may need to present their NRIC or Photo ID for authentication of identity&nbsp;</p>
<p><strong>For Delivery: </strong></p>
<p>For delivery, please email to <a href="mailto:onlinesales@parisilk.com">onlinesales@parisilk.com</a> with the following details:<br />◦ Name<br />◦ Contact Number<br />◦ Delivery Address<br />◦ Attached Voucher<br />&bull; We will be calling you to confirm your delivery date &amp; timing at least 1 day before delivery. Please allow 3 days for delivery upon confirmation<br />&bull; For enquiries, please call 64712329<strong>&nbsp;</strong></p>
<p><strong>PaRiSiLk&nbsp;Electronics &amp; Computers&nbsp;Pte&nbsp;Ltd</strong></p>
<p><strong>North Outlet</strong><br />58&nbsp;Sembawang&nbsp;Road,<br />#01-02/03, Hong&nbsp;Heng&nbsp;Mansions<br />Singapore 779087</p>
<p><strong>Central Outlet</strong><br />No&nbsp;15A&nbsp;Lorong&nbsp;Liput<br />(Holland Village)<br />Singapore 277730</p>
<p><strong>East Outlet</strong>&nbsp;<br />46 East Coast Road<br />#01-01,&nbsp;Eastgate<br />Singapore 428766</p>
<p><strong>East Outlet 2<br /></strong>Blk 214 Bedok North St 1<br />#01-179 Bedok Central<br />Singapore 460214&nbsp;</p>
<p><strong>Redemption Hours:</strong><br />11am&nbsp;to 7:30pm&nbsp;(Mon to Sat)<br />Closed on Sun, Eve of Public Holidays &amp; Public Holidays</p>
<p align="center"><strong>Mistral<br /></strong>Power Fan 3x6in Fan<br />(MDC306GW)<br />3 YEARS MOTOR WARRANTY</p>
<p align="center"><strong>FEATURES</strong></p>
<ul>
<li style="text-align: center;">3 separate fan blades</li>
<li style="text-align: center;">Wide angle 235 degree oscillation</li>
<li style="text-align: center;">Variable speed control</li>
<li style="text-align: center;">Energy Saving DC Motor (saves up to 60%)</li>
<li style="text-align: center;">Voltage: 220-240V~50/60hz</li>
<li style="text-align: center;">Power 8-33W</li>
<li style="text-align: center;">Dimensions: approx. 104cm (Height) x 21cm (Base Diameter)</li>
</ul>
<p style="text-align: center;" align="center">&nbsp;<img src="https://www.imobshop.sg/media/wysiwyg/image1_24.jpg" alt="" /></p>
<p style="text-align: center;" align="center"><img src="https://www.imobshop.sg/media/wysiwyg/image2_31.jpg" alt="" /></p>
<p style="text-align: center;" align="center"><img src="https://www.imobshop.sg/media/wysiwyg/image3_24.jpg" alt="" /></p>
<p style="text-align: center;" align="center"><img src="https://www.imobshop.sg/media/wysiwyg/image4_19.jpg" alt="" /></p>
<p style="text-align: center;" align="center"><img src="https://www.imobshop.sg/media/wysiwyg/image5_17.jpg" alt="" /></p>
<p align="center"><img src="https://www.imobshop.sg/media/wysiwyg/1st_ParisilkLogo.png" alt="" /></p>
<p align="center"><img src="https://www.imobshop.sg/media/wysiwyg/Last_Redemption_Info.JPG" alt="" /></p>    </div>
</div>
	  	  	  	  <div id="product_tabs_additional_contents" class="prouct_tabs">    <h2>Additional Information</h2>
    <table class="data-table" id="product-attribute-specs-table">
        <col width="25%" />
        <col />
        <tbody>
                    <tr>
                <th class="label">Seller Name</th>
                <td class="data">NA</td>
            </tr>
                    <tr>
                <th class="label">Seller Email</th>
                <td class="data">NA</td>
            </tr>
                    <tr>
                <th class="label">Seller Address</th>
                <td class="data">NA</td>
            </tr>
                    <tr>
                <th class="label">Seller Postal Code</th>
                <td class="data">NA</td>
            </tr>
                    <tr>
                <th class="label">Seller Phone</th>
                <td class="data">NA</td>
            </tr>
                    <tr>
                <th class="label">Terms and Conditions</th>
                <td class="data">Refer to " Details "</td>
            </tr>
                    <tr>
                <th class="label">Details</th>
                <td class="data"><p><span style="text-decoration: underline;"><strong>Terms and Conditions</strong></span><br /><br />Return Policy:<br /><span>Voucher is valid within 2 months upon purchase.</span><br />We offer 1 for 1 exchange for items with manufacturing defect. Please contact us within 7 days for an exchange at&nbsp;<a href="mailto:onlinesales@parisilk.com">onlinesales@parisilk.com</a>&nbsp;or&nbsp;64712329.</p>
<p><strong><span style="text-decoration: underline;">Redemption Details<br /></span></strong><strong>For Self-Collection: </strong></p>
<p>Redemption Details<br />&bull; For self-collection, reservation is strictly required; please call 64712329 and quote "iMob" at least 1 day in advance before coming down to redeem your product<br />&bull; Please refer below for redemption locations<br />&bull; Timing: 11am to 7.30pm (Mon - Sat)<br />&bull; <strong>Printed voucher must be presented upon redemption<br /></strong>&bull; Buyers may need to present their NRIC or Photo ID for authentication of identity&nbsp;</p>
<p><strong>For Delivery: </strong></p>
<p>For delivery, please email to <a href="mailto:onlinesales@parisilk.com">onlinesales@parisilk.com</a> with the following details:<br />◦ Name<br />◦ Contact Number<br />◦ Delivery Address<br />◦ Attached Voucher<br />&bull; We will be calling you to confirm your delivery date &amp; timing at least 1 day before delivery. Please allow 3 days for delivery upon confirmation<br />&bull; For enquiries, please call 64712329<strong>&nbsp;</strong></p>
<p><strong>PaRiSiLk&nbsp;Electronics &amp; Computers&nbsp;Pte&nbsp;Ltd</strong></p>
<p><strong>North Outlet</strong><br />58&nbsp;Sembawang&nbsp;Road,<br />#01-02/03, Hong&nbsp;Heng&nbsp;Mansions<br />Singapore 779087</p>
<p><strong>Central Outlet</strong><br />No&nbsp;15A&nbsp;Lorong&nbsp;Liput<br />(Holland Village)<br />Singapore 277730</p>
<p><strong>East Outlet</strong>&nbsp;<br />46 East Coast Road<br />#01-01,&nbsp;Eastgate<br />Singapore 428766</p>
<p><strong>East Outlet 2<br /></strong>Blk 214 Bedok North St 1<br />#01-179 Bedok Central<br />Singapore 460214&nbsp;</p>
<p><strong>Redemption Hours:</strong><br />11am&nbsp;to 7:30pm&nbsp;(Mon to Sat)<br />Closed on Sun, Eve of Public Holidays &amp; Public Holidays</p></td>
            </tr>
                </tbody>
    </table>
    <script type="text/javascript">decorateTable('product-attribute-specs-table')</script>
</div>
	  	  	  	  <div id="product_tabs_reviews_contents" class="prouct_tabs">
<div class="box-collateral box-reviews" id="customer-reviews">
        </div>
</div>
	  	  	  	  <div id="product_tabs_addreviews_contents" class="prouct_tabs"><div class="form-add">
    <h2>Write Your Own Review</h2>
        <p class="review-nologged" id="review-form">
        Only registered users can write reviews. Please, <a href="https://www.imobshop.sg/customer/account/login/referer/aHR0cHM6Ly93d3cuaW1vYnNob3Auc2cvY2F0YWxvZy9wcm9kdWN0L3ZpZXcvaWQvODc5L2NhdGVnb3J5LzEwLz9fX19TSUQ9VSNyZXZpZXctZm9ybQ,,/">log in</a> or <a href="https://www.imobshop.sg/customer/account/create/">register</a>    </p>
    </div>
</div>
	  	  	    </div>
  </div>

  <div class="clearall"></div>
<script type="text/javascript">
//<![CDATA[

function doShowReviews(id)
{
	var lis = document.getElementById('tabs').getElementsByTagName("li");
	for(var i=0;i<lis.length;i++)
	{
 		if(lis[i].id=='product_tabs_reviews')
		{
			lis[i].className = 'active';
			lis[i].style.display='block';
			document.getElementById('product_tabs_reviews_contents').style.display='block';
		}
		else
		{
			lis[i].className = '';
			document.getElementById(lis[i].id+'_contents').style.display='none';
		}
	}
	if(location.href.indexOf('product_tabs_reviews')== -1)
	{
		location.href = location.href+"#product_tabs_reviews";
	}
	else
	{
		location.href = location.href;
	}
}
function doShowReviewform(id)
{
	var lis = document.getElementById('tabs').getElementsByTagName("li");
	for(var i=0;i<lis.length;i++)
	{
 		if(lis[i].id=='product_tabs_addreviews')
		{
			lis[i].className = 'active';
			lis[i].style.display='block';
			document.getElementById('product_tabs_addreviews_contents').style.display='block';
		}
		else
		{
			lis[i].className = '';
			document.getElementById(lis[i].id+'_contents').style.display='none';
		}
	}
}


Varien.Tabs = Class.create();
Varien.Tabs.prototype = {
  initialize: function(selector) {
    var self=this;
    $$(selector+' a').each(this.initTab.bind(this));
  },

  initTab: function(el) {
      el.href = 'javascript:void(0)';
      if ($(el.parentNode).hasClassName('active')) {
        this.showContent(el);
      }
      el.observe('click', this.showContent.bind(this, el));
  },

  showContent: function(a) {
    var li = $(a.parentNode), ul = $(li.parentNode);
    ul.getElementsBySelector('li', 'ol').each(function(el){
      var contents = $(el.id+'_contents');
      if (el==li) {
        el.addClassName('active');
        contents.show();
      } else {
        el.removeClassName('active');
        contents.hide();
      }
    });
  }
}
new Varien.Tabs('.tabs');
//]]>
</script>

    </div>
</div>
<script type="text/javascript">
    var lifetime = 3600;
    var expireAt = Mage.Cookies.expires;
    if (lifetime > 0) {
        expireAt = new Date();
        expireAt.setTime(expireAt.getTime() + lifetime * 1000);
    }
    Mage.Cookies.set('external_no_cache', 1, expireAt);
</script>
                </div>
            </div>
        </div>
        <div class="customeditedbyzinfooter-container">
<div class="newaletter">
<p>
<div class="bgcustomeditbyz">&nbsp;</div>
<div class="customfootereditbyz">
<div class="footer_link_box">

<div class="link">
<h1>About iMOB Shop</h1>
<ul>
<li title="About Us"><a href="https://www.imobshop.sg/about-imob/">About Us</a></li>
<li title="T&amp;C"><a href="https://www.imobshop.sg/tnc/">T&amp;Cs</a></li>
<li title="Privacy Policy"><a href="https://www.imobshop.sg/privacy-policy/">Privacy Policy</a></li>
</ul>
</div>
<div class="link">
<h1>Get On Board</h1>
<ul>
<li title="Register"><a href="https://www.imobshop.sg/customer/account/create/">Register</a></li>
<li title="Facebook"><a href="https://www.facebook.com/iMOBsg">Facebook</a></li>
</ul>
</div>
<div class="link">
<h1>Download Our Mobile Apps</h1>
<ul>
<li title="GooglePlay"><a href="https://play.google.com/store/apps/details?id=smrt.media.imobshop"> <img style="width: 80%; margin-bottom: 5px;" src="https://www.imobshop.sg/media/brandlogo/android.gif" alt="" /></a></li>
<li title="AppStore"><a href="https://itunes.apple.com/sg/app/imob-shop/id932000617?mt=8&amp;ign-mpt=uo%3D4"><img style="width: 80%;" src="https://www.imobshop.sg/media/brandlogo/ios.gif" alt="" /></a></li>
</ul>
</div>
<div class="link">
<h1>Customer Service</h1>
<ul>
<li title="FAQ"><a href="https://www.imobshop.sg/faq/">FAQ</a></li>
<li title="Contact Us"><a href="https://www.imobshop.sg/contacts/">Contact Us</a></li>
</ul>
</div>
<div class="link">
<h1>Official Card</h1>
<ul>
<li title="Citi"><a href="https://www.citibank.com.sg/gcb/credit_cards/citi_smrt_card.htm?icid=SGCCASPENCCHOCB06"><img src="https://www.imobshop.sg/skin/frontend/default/metrostore/images/CITI.png" alt="We Accept all Major Credit Cards" width="100" /></a></li>
<li title="Payment"><!--<img style="margin-top: 10px;" src="/skin/frontend/default/metrostore/images/Visa_Logo.png" alt="We Accept all Major Credit Cards" width="100" />--></li>
</ul>
</div>
<div class="link last">
<h1>I'm on board the latest</h1>
<h1 style="margin-top: -10px;">lifestyle iSpace</h1>
<p>Send me the hottest trends, savings, offers &amp; information.</p>
<div class="formwidthcustom">
<form action="https://www.imobshop.sg/newsletter/subscriber/new/" method="post" id="newsletter-validate-detail">


            <div class="custominputeditbyz">
               <input type="text" name="email" id="newsletter" value="Enter Your Email" onfocus="this.value=''" title="Sign up for our newsletter" class="input-text required-entry validate-email" />


                <button type="submit" title="Subscribe" class="button"><span><span>GO</span></span></button>
            </div>

    </form>
	</div>
</div>
</div>
</div>


<script type="text/javascript">
//<![CDATA[
	var newsletterSubscriberFormDetail = new VarienForm('newsletter-validate-detail');
//]]>
</script>

</p>
</div></div>

<div class="footer-container">

    <div class="footer">

        <div class="custompayment"><img class="custommaster" src="https://www.imobshop.sg/skin/frontend/default/metrostore/images/Mastercard.png" alt="We Accept all Mastercard Cards" width="100" /> <img class="customvisa" src="https://www.imobshop.sg/skin/frontend/default/metrostore/images/VISA.png" alt="We Accept all VISA Cards" width="100" /> <a onclick="window.open('https://www.sitelock.com/verify.php?site=imobshop.sg','SiteLock','width=600,height=600,left=160,top=170');" href="#"><img class="customsite8" title="SiteLock" src="//shield.sitelock.com/shield/imobshop.sg" alt="website security" /></a><a onclick="window.open('https://seal.starfieldtech.com/verifySeal?sealID=162kjXVq5OqroQfQplOOtshsxVKXT97PkNX8J7gPOcVF7rXYDnqhjnL0CbCb','Secure SSL','width=600,height=600,left=160,top=170');" href="#"><img class="customsecure" src="https://www.imobshop.sg/skin/frontend/default/metrostore/images/ssl_verified_logo_09.png" alt="Secure SSL" /> </a></div>

        <address>&copy; iMOB Shop. All Rights Reserved.</address>
<!--<div style="align:center; margin-bottom:5px;">
<img style="margin-right: 5px;" src="http://www.imobshop.sg/media/brandlogo/SSL.gif" alt="" /><a  href="#">
<img title="SiteLock" src="//shield.sitelock.com/shield/imobshop.sg" alt="website security" /></a></div>-->
    </div>
</div>



    </div>
</div>
</body>
</html>


'''


''''''''''''''''''''''''''''''''''''''''''''''''''
print int(time.time())
hsl = Selector(text=html)
str_xml = file( os.getcwd() + '/spider/spiders/website/imobshop.xml','a+').read()
xsl = Selector(text=str_xml, type='xml')
# special-price
# regular-price
# special-price
# print hsl.xpath("//p[@class='special-price']//span[@class='price']/text()").extract()
# print hsl.xpath("//span[@class='regular-price']//span[@class='price']/text()").extract()
item = match_dmoz_field(text=html, xml=xsl)
print item
''''''''''''''''''''''''''''''''''''''''''''''''''