package com.example.mybatis.controller;

import com.example.mybatis.entity.User;
import com.example.mybatis.service.IUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
/*
 * 1.@RestController---添加控制层注解，让springboot知道这是控制层
 * 2.@RequestMapping("/user")--- user代表默认访问路径在/user下可以访问
 * */

@RestController
@RequestMapping("/user")
public class UserController {


    @Autowired  //4.自动注解
    private IUserService userService;  //3.定义调用服务层的接口


    /*
    *5.查询全部的数据
       5.1使用 @GetMapping注解，没有括号不定义就代表使用get方式，url访问上面默认路径/user
       5.2查询全部肯定使用的方法是集合<实体类>方式去自定义一个findAll方法名
       5.3再用服务层返回一个集合就好了
     */
    @GetMapping
    public List<User> findAll(){
        return userService.list();
    }


    /*6.根据id查询一条
      6.1查询使用@GetMapping注解，既然是根据id查询，那么就要把id传给后端。但是get是不能传递请求体的，
       只能传递请求头，那么只能把这个值放在请求头上面，就是这样("/{id}")放
      6.2自定义一个方法名(@PathVariable 类型 id),为什么要用id呢？这不是你前端这个"/{id}"说要吗
      @PathVariable这个注解的方式就是把请求头中的数字以Json传递给后端去识别，后端不能直接识别url上面的数字
      6.3 再用服务层返回获取id的方法就好了
    */
    @GetMapping("/{id}")
    public User findById(@PathVariable Integer id){
        return userService.getById(id);
    }

    /*7.新增和修改
         需要传递body传递全部参数，
        7.1对数据的操作使用@PostMapping，括号里面不定义就代表使用post方式，url访问上面默认路径/user
        7.2自定义一个方法，括号里面使用(@RequestBody 属性类 自定义属性昵称)
        为什么这里用Boolean而不是User，因为对数据的修改希望返回的结果就两种，要么成功，要么失败，所以用布尔值
        @RequestBody这个注解用于映射传递来的json参数映射为到java对象里面，特别是适用与请求体的参数
        7.3然后再用服务层返回获取的saveOrUpdate方法就好了
    */
    @PostMapping
    public Boolean add(@RequestBody User user){
        return userService.saveOrUpdate(user);
    }
    /*
    8.删除的方法
     8.1使用@DeleteMapping注解，因为删除只需要传递一个特定的id给后端就可以了，
     所以括号里面使用("/{id}")
     8.2创建一个自定义的方法，删除也是要么成功要么失败，所以使用Boolean作为返回值
     @PathVariable在上面已经解释过了
     8.3再用服务层次返回对应的方法，括号里面的值就是上面括号里面需要的值
    * */
    @DeleteMapping("/{id}")
    public Boolean delete(@PathVariable Integer id){
        return userService.removeById(id);
    }

    @PostMapping("/update")
    public Boolean update(@RequestBody User user){
        return userService.updateById(user);
    }

}








/*    //修改数据的另一种写法
    @PostMapping("/update")
    public Boolean update(@RequestBody User user){
        return userService.updateById(user);
    }*/