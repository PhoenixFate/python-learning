from redis import StrictRedis


def main():
    # 创建一个StrictRedis对象，连接redis
    try:
        strict_redis = StrictRedis(host='114.67.89.253', port=6379, db=9, password="centos123qwer")
        # String 类型；设置key value
        # set: 如果不存在key，则设置，如果存在，则修改
        result = strict_redis.set(name="name", value="tom")
        print(result)
        # 获取值
        name = strict_redis.get("name")
        print("name: %s" % name)
        # 删除key以及对应的值
        result = strict_redis.delete("name")
        print("delete: %d" % result)
        # 删除多个key value
        strict_redis.set(name="name", value="tom")
        strict_redis.set(name="name1", value="tom1")
        result = strict_redis.delete("name", "name1")
        print("delete: %d" % result)

        # 获取所有的key pattern默认为*
        strict_redis.set(name="name", value="tom")
        strict_redis.set(name="name1", value="tom1")
        result = strict_redis.keys(pattern="*")
        print(result)
        pass
    except Exception as e:
        print(e)
        pass

    pass


if __name__ == '__main__':
    main()
