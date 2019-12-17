<?php
    function testAddOne($value) {
        echo 1 + $value;
    }
?>

<h1>
    <?php 
        bloginfo('name');
    ?>
</h1>

<p>
    <?php 
        bloginfo('description');
        echo nl2br("\n");
        testAddOne(4);
    ?>
</p>