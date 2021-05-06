from services.percentile_factory import PercentileFactory

POOL_LIST = [
    {
        'poolId': 1,
        'poolValues': [1,2,3,4,5]
    },
    {
        'poolId': 2,
        'poolValues': [2,3,3.7,5]
    },
    {
        'poolId': 3,
        'poolValues': [1, 3, 5, 6, 9, 11, 12, 13, 19, 21, 22, 32, 35, 36, 45, 44, 55, 68, 79, 80, 81, 88, 90, 91, 92, 100, 112, 113, 114, 120, 121, 132, 145, 146, 149, 150, 155, 180, 189, 190]
    }
]

class PoolHandler():
    @classmethod
    def validate(cls, pool):
        if 'poolId' not in pool:
            return 'Pool id is not existed'
        if 'poolValues' not in pool:
            return 'Pool values is not existed'
        return True

    @classmethod
    def insert(cls, pool):
        POOL_LIST.append(pool)
        return True

    @classmethod
    def update(cls, pool):
        for item in POOL_LIST:
            if item['poolId'] == pool['poolId']:
                item['poolValues'].extend(pool['poolValues'])
                return True
        return 'Not exist pool'
        

    @classmethod
    def upsert(cls, pool):
        validate_pool = cls.validate(pool)
        if validate_pool != True:
            return validate_pool
        res = cls.update(pool)
        if res == True:
            return 'Appended'
        cls.insert(pool)
        return 'Inserted'


    @classmethod
    def get_pool_values(cls, pool_id):
        for item in POOL_LIST:
            if item['poolId'] == pool_id:
                return item['poolValues']
        return False


    @classmethod
    def get(cls, posted_obj, strategy):
        if 'poolId' not in posted_obj:
            return 'There is not pool id in parameters'
        if 'percentile' not in posted_obj:
            return 'There is not percentile in parameters'

        pool_id = posted_obj['poolId']
        percentile = posted_obj['percentile']

        pool_values = cls.get_pool_values(pool_id)
        if pool_values == False:
            return 'There is not matching pool with given pool id'

        handler = PercentileFactory.create_strategy(percentile, pool_values, strategy)
        if handler is None:
            return 'There is not valid strategy handler'

        result = handler.get_indexes()
        return result
        if (not isinstance(result, dict)):
            return False, result
        return True, result
        