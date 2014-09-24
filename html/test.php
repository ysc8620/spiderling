<?php


$conn = new Mongo("127.0.0.1");
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
        $row = $table->find(array('_id'=>$item['_id']));
        print_r($row);
    }
}
?>