<?php


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

        print_r($item);
        $objectId = new MongoId($item['_id']);
        $row = $table->findOne(array('_id'=>$objectId));
        var_dump($row);
    }
}
?>