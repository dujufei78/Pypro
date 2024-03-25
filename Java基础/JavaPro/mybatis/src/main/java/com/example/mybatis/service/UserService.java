package com.example.mybatis.service;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.mybatis.entity.User;
import com.example.mybatis.mapper.UserMapper;
import org.springframework.stereotype.Service;

/*
 * 1.使用@Service注解，要不然咱自己定义的类，谁知道他是服务层
 * 2.继承ServiceImpl，这个是MP内置增删改查接口的一个实现，牛逼的是还能自定义直接调取数据层的数据
 * 3.定义需要的方法，根据自己的需要定义，定义MP内置里面没有的
 * */
@Service
public class UserService extends ServiceImpl<UserMapper, User> {
    //下面这个方法是对数据库操作时候多加了一层封装，用不到去掉也没有影响。
    // 、作用可以定义密码加密、数据校验、关联数据处理、日志记录、通知或触发事件等
    public boolean saveUser(User user){
        return saveOrUpdate(user);
    }
}