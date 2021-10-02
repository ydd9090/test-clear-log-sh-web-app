#! /usr/bin/bash
warnDir=/app/logs/*/warn
infoDir=/app/logs/*/info
today=`date +%Y-%m-%d`

usedRate=`df /app | awk 'NR==2{print $5}'` # 获取日志磁盘空间使用率,根据实际情况调整取值方式
if [[ ${usedRate} >= 80% ]];then
    echo "磁盘空间使用率超过80%，开始清理日志...,仅保留当天的日志"
    echo "清理warn目录日志"
    for $file in `ls ${warnDir}`;do
        if [[ warn-${today}.log > $file ]];then
            rm -rf ${warnDir}/${file}
        fi
    done
    echo "清理完成"
    echo "清理info目录日志"
    for $file in `ls ${infoDir}`;do
        if [[ info-${today}.log > $file ]];then
            rm -rf ${infoDir}/${file}
        fi
    done
fi

echo "清理完成"
usedRate=`df /app | awk 'NR==2{print $5}'`
echo "清理后磁盘空间使用率为:${usedRate}"