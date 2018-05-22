function getAgentInfo(){
        $agent = $_SERVER['HTTP_USER_AGENT'];
        $brower = array(
            'MSIE' => 1,
            'Firefox' => 2,
            'QQBrowser' => 3,
            'QQ/' => 3,
            'UCBrowser' => 4,
            'MicroMessenger' => 9,
            'Edge' => 5,
            'Chrome' => 6,
            'Opera' => 7,
            'OPR' => 7,
            'Safari' => 8,
            'Trident/' => 1
        );
        $system = array(
            'Windows Phone' => 4,
            'Windows' => 1,
            'Android' => 2,
            'iPhone' => 3,
            'iPad' => 5
        );
        $browser_num = 0;//未知
        $system_num = 0;//未知
        foreach($brower as $bro => $val){
            if(stripos($agent, $bro) !== false){
                $browser_num = $val;
                break;
            }
        }
        foreach($system as $sys => $val){
            if(stripos($agent, $sys) !== false){
                $system_num = $val;
                break;
            }
        }
        return array('sys' => $system_num, 'bro' => $browser_num);
    }
