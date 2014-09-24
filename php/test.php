<?php


$conn = new Mongo("127.0.0.1");
echo $conn->test->goods->find()->count();

require 'vendor/autoload.php';

$client = new Elasticsearch\Client(array("hosts"=>array("host"=>"127.0.0.1", "port"=>"9200")));

#$query  = new Elasticsearch\Elastica\Query();

$searchParams['index'] = 'goods-index';
$searchParams['type']  = 'goods-type';
$searchParams['from'] = 0;
$searchParams['size'] = 12;
#$searchParams['body']['query']['match']['title'] = 'iphone';
$queryResponse = $client->search($searchParams);

print_r($queryResponse);