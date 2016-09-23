# import time
# def GetNowTime():
#     return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
#
# print(GetNowTime())

a = """
root 9655 1 0 14:41 ? 00:00:30 /usr/java/jdk1.8.0_51/bin/java -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -Djava.awt.headless=true -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+HeapDumpOnOutOfMemoryError -Xmx1g -Xss2048k -Djffi.boot.library.path=/data/logstash-2.3.4/vendor/jruby/lib/jni -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -Djava.awt.headless=true -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/data/logstash-2.3.4/heapdump.hprof -Xbootclasspath/a:/data/logstash-2.3.4/vendor/jruby/lib/jruby.jar -classpath :.:/home/download/jdk1.8.0_20/lib/dt.jar:/home/download/jdk1.8.0_20/lib/tools.jar:/home/download/jdk1.8.0_20/jre/lib::/home/jdk1.8.0_20/lib:/home/jdk1.8.0_20/jre/jre/lib:/usr/java/jdk1.8.0_51/lib:/home/jdk1.8.0_20/jre/jre/lib -Djruby.home=/data/logstash-2.3.4/vendor/jruby -Djruby.lib=/data/logstash-2.3.4/vendor/jruby/lib -Djruby.script=jruby -Djruby.shell=/bin/sh org.jruby.Main --1.9 /data/logstash-2.3.4/lib/bootstrap/environment.rb logstash/runner.rb agent -f /data/logstash-2.3.4/conf/solficm.conf
Back Home Page
"""
print(len(a.split()))