# Neo4j



Neo4j是一种高性能的NoSQL图形数据库，它以图的形式存储数据，专为处理高度连接的数据而设计。与传统的关系型数据库不同，它采用图形结构来存储和查询数据，使其非常适合处理复杂的网络和关系。



**Neo4j的主要特点和功能的详细介绍**

1. **图形数据模型**：Neo4j使用图形数据模型来表示数据。在这个模型中，数据以节点（entities）和边（relationships）的形式存在。节点代表实体，如人、地点或事物，而边代表实体之间的关系。这种模型直观地表达了实体间的复杂关系。

2. **Cypher查询语言**：Neo4j引入了一种专门的查询语言——Cypher。Cypher设计简洁，易于学习，能够有效地执行复杂的图形查询和操作。它使用类似ASCII艺术的语法来描述图形模式，使得查询更直观。

3. **性能**：由于其图形数据结构的本质，Neo4j在处理大规模、高度连接的数据时能够提供卓越的性能。它能快速处理复杂的查询，尤其是涉及深层连接和模式匹配时。

4. **可扩展性**：Neo4j支持水平和垂直扩展。这意味着随着数据量的增加，它可以通过增加更多的服务器来提高处理能力。

5. **事务支持**：Neo4j支持ACID事务（原子性、一致性、隔离性、持久性），这对于需要高数据完整性的应用来说是非常重要的。

6. **集成和兼容性**：Neo4j可以与多种编程语言和框架集成，包括Java、Python、JavaScript等。此外，它还提供了REST API，使得它可以轻松地与其他应用和服务集成。

7. **应用场景**：Neo4j广泛应用于多种领域，包括社交网络分析、推荐系统、欺诈检测、网络和IT运营、生物信息学等。

8. **社区和资源**：Neo4j拥有一个活跃的开发者社区，提供大量的文档、教程和案例研究，有助于新用户快速上手和使用。

9. **企业特性**：对于企业用户，Neo4j提供额外的特性，如高可用性集群、高级监控、安全性控制等。



### 高级特性

1. **索引和约束**：Neo4j支持创建索引以加快特定节点和关系的查询速度。此外，还可以定义约束来确保数据的完整性，如唯一性约束。

2. **路径查找和模式匹配**：Neo4j特别擅长执行复杂的路径查找和模式匹配查询，这对于诸如社交网络分析、路由优化等应用至关重要。

3. **存储过程和用户定义函数**：用户可以编写自定义的存储过程和函数，这些可以用于执行复杂的数据处理和业务逻辑。

4. **图形算法库**：Neo4j提供了一系列内置的图形算法，如路径查找、中心性分析和社区检测，这些都是分析复杂网络结构的强大工具。



### 实际应用场景

1. **社交网络**：在社交网络分析中，Neo4j能够有效地处理和分析复杂的社交关系，如朋友网络、推荐朋友、社交影响力分析等。

2. **推荐系统**：利用Neo4j的图形结构和查询能力，可以构建高效的推荐系统，为用户推荐产品、服务或内容。

3. **欺诈检测**：在金融服务领域，Neo4j能够帮助识别异常模式和关系网络，从而有效地检测和预防欺诈行为。

4. **供应链优化**：在物流和供应链管理中，Neo4j可以帮助企业优化其供应链网络，提高效率并降低成本。

5. **网络和IT基础设施**：对于网络和IT基础设施管理，Neo4j可以帮助跟踪和分析网络组件之间的复杂关系，提高故障检测和解决问题的效率。

6. **生命科学和健康数据分析**：Neo4j在生命科学领域被用于基因组学、蛋白质网络分析和药物发现等复杂的生物数据分析。



### 技术集成和开发

1. **API和驱动程序**：Neo4j提供了多种语言的驱动程序和API，支持Java、Python、JavaScript、.NET等。

2. **图形数据科学平台**：Neo4j还提供了一个图形数据科学平台，该平台集成了图形数据库和图形算法，使数据科学家能够更容易地进行复杂的图形分析。

3. **云服务和部署**：Neo4j提供了云服务解决方案，如Neo4j Aura，使用户能够在云中轻松部署和管理图形数据库。

4. **社区和支持**：Neo4j有一个庞大且活跃的社区，提供丰富的资源、论坛和支持，这对于新用户和经验丰富的开发者都非常有用。





### 使用 Docker 启动 Neo4服务

```shell
docker run -tid \
	--restart=always \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --env NEO4J_AUTH=neo4j/12345678 \
    --name neo4j \
    neo4j:4.0
```





## Python与Neo4j

#### 安装Python驱动

使用pip安装Neo4j Python驱动：

```bash
pip install neo4j
```



### 基本操作



#### 连接到Neo4j

使用Python连接到Neo4j数据库：

```python
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "12345678"))
```



#### 创建节点和关系

在Python中使用Neo4j创建节点和关系的示例：

```python
def create_graph(tx):
    # 创建节点
    tx.run("CREATE (a:Person {name: 'zhuzhiwei', age: 26})")
    tx.run("CREATE (b:Person {name: 'dujufei', age: 28})")
    tx.run("CREATE (b:Person {name: 'liuhanyang', age: 25})")
    tx.run("CREATE (b:Person {name: 'yunchuan', age: 24})")

    # 创建关系
    tx.run("MATCH (a:Person), (b:Person) "
           "WHERE a.name = 'zhuzhiwei' AND b.name = 'dujufei' "
           "CREATE (a)-[r:认识]->(b) "
           "RETURN type(r)")
    
    # 创建关系
    tx.run("MATCH (a:Person), (b:Person) "
           "WHERE a.name = 'zhuzhiwei' AND b.name = 'liuhanyang' "
           "CREATE (a)-[r:认识]->(b) "
           "RETURN type(r)")

    # 创建关系
    tx.run("MATCH (a:Person), (b:Person) "
           "WHERE a.name = 'dujufei' AND b.name = 'yunchuan' "
           "CREATE (a)-[r:认识]->(b) "
           "RETURN type(r)")
           
# 创建图
with driver.session() as session:
    session.execute_write(create_graph)
```



### 查询和分析

使用Cypher查询语言，你可以在Python中执行复杂的图形查询和分析。例如，要查找与特定节点直接连接的所有节点：

```python
def find_friends(tx, name):
    friends = tx.run("MATCH (a:Person)-[:认识]->(b) "
                     "WHERE a.name = $name "
                     "RETURN b.name", name=name)
    return [record["b.name"] for record in friends]



# 查找朋友
with driver.session() as session:
    friends_of_zhuzhiwei = session.execute_read(find_friends, "zhuzhiwei")
    for name in friends_of_zhuzhiwei:
        print(name)
```



### 关闭连接

完成操作后，确保关闭与Neo4j的连接：

```python
driver.close()
```



# Cypher查询语言

Cypher是Neo4j图形数据库的查询语言，专门设计用来方便地表达和处理图形数据。它的语法是声明式的，意味着你可以描述你想要的数据，而不是描述如何获取这些数据。



### 节点和关系

- **节点（Nodes）**：图形中的实体，如人、地点或物体。在Cypher中，节点用圆括号表示，例如 `(n)`。
- **关系（Relationships）**：连接节点的线，表示节点之间的关系。在Cypher中，关系用方括号和短横线表示，例如 `-[r]->` 或 `<-[r]-`。

### 创建数据（CREATE）

创建节点和关系的基本语法如下：

```cypher
CREATE (n:Label {propertyKey: 'propertyValue', ...})
```

例如，创建一个名为"Alice"的人和：

```cypher
CREATE (a:Person {name: 'Alice', sex: 1})
```

例如，创建一个表示Alice认识Bob的关系：

```cypher
CREATE (a:Person {name: 'Alice'})-[r:KNOWS]->(b:Person {name: 'Bob'})
```

### 查询数据（MATCH）

查询数据通常使用 `MATCH` 语句。你可以使用模式匹配来找到满足特定条件的节点和关系。

例如，查找所有的Person节点：

```cypher
MATCH (n:Person)
RETURN n
```

查找名为"Alice"的人：

```cypher
MATCH (n:Person {name: 'Alice'})
RETURN n
```

### 更新数据（SET）

更新节点或关系的属性：

```cypher
MATCH (n:Person {name: 'Alice'})
SET n.age = 31
RETURN n
```

这会将名为Alice的人的年龄更改为31。

### 删除数据（DELETE）

删除节点和关系：

```cypher
MATCH (n:Person {name: 'Alice'})
DETACH DELETE n
```

`DETACH DELETE` 用于删除节点及其所有关系。如果只使用 `DELETE`，则必须先删除所有关系。

### 路径和模式

Cypher非常擅长处理路径和模式。例如，找到两个人之间的路径：

```cypher
MATCH path = (a:Person {name: 'zhuzhiwei'})-[*]-(b:Person {name: 'yunchuan'})
RETURN path
```

这将返回zhuzhiwei和yunchuan之间的所有路径。



### 聚合和排序

使用聚合函数和排序：

```cypher
MATCH (n:Person)
RETURN n.age, COUNT(n) AS NumberOfPeople
ORDER BY n.age
```

这将返回按年龄分组的人数。



PS:   **快速清除容器里已经创建的数据**

```shell
docker stop neo4j

sudo rm -rf $HOME/neo4j/data/*

docker restart neo4j
```
