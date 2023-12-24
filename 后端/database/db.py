from neo4j import GraphDatabase
import threading
import logging
from neo4j.exceptions import ServiceUnavailable

uri = "bolt://localhost:7687"
password = "12345678"
user = "neo4j"


class DB:
    def __init__(self):
        self.local = threading.local()

    def get_driver(self):
        if not hasattr(self.local, "driver") or self.local.driver is None:
            self.local.driver = GraphDatabase.driver(uri, auth=(user, password))
        return self.local.driver

    def close(self):
        if hasattr(self.local, "driver") and self.local.driver is not None:
            self.local.driver.close()
            self.local.driver = None





    @staticmethod
    def _create_node(tx, label, properties):
        query = f"CREATE (n:{label} $properties) RETURN n"
        result = tx.run(query, properties=properties)
        return result.single()[0]

    def get_node_by_id(self, node_id):
        driver = self.get_driver()
        with driver.session(database='disease') as session:
            node = session.read_transaction(self._get_node_by_id, node_id)
        return node

    def get_node_by_name(self, node_id):
        driver = self.get_driver()
        with driver.session(database='disease') as session:
            node = session.read_transaction(self._get_node_by_name, node_id)
        return node

    @staticmethod
    def _get_node_by_id(tx, node_id):
        query = "MATCH (n) WHERE id(n) = $node_id RETURN n"
        result = tx.run(query, node_id=node_id)
        return result.single()[0]

    @staticmethod
    def _get_node_by_name(tx, node_id):
        query = "MATCH (n) WHERE n.name = $node_id RETURN n"
        result = tx.run(query, node_id=node_id)
        record = result.single()
        if record is not None:
            return record[0]
        else:
            return None
    # def _get_node_by_name(tx, node_id):
    #     query = "MATCH (n) WHERE n.name = $node_id RETURN n"
    #     result = tx.run(query, node_id=node_id)
    #     return result.single()[0]

    def get_nodes(self, label):
        driver = self.get_driver()
        with driver.session() as session:
            nodes = session.read_transaction(self._get_nodes, label)
        return nodes

    @staticmethod
    def _get_nodes(tx, label):
        query = f"MATCH (n:{label}) RETURN n"
        result = tx.run(query)
        nodes = [record[0] for record in result]
        return nodes

    # def __init__(self):
    #     uri = "neo4j+s://06bef84e.databases.neo4j.io"
    #     password = "guw5huMp62eVSJMojt3HC2XLwdQ2oTlItmEmLDsmBx8"
    #     user = "neo4j"
    #     self.driver = GraphDatabase.driver(uri, auth=(user, password))

    # def close(self):
    #     # Don't forget to close the driver connection when you are finished with it
    #     self.driver.close()

    def find_all_disease(self):
        driver = self.get_driver()
        with driver.session(database="disease") as session:
            result = session.run("MATCH (d:disease) RETURN d.name AS name")
            # Build the result list
            results = []
            for i, record in enumerate(result):
                results.append({'id': i, 'name': record['name']})
            return results

    def find_all_item(self):
        driver = self.get_driver()
        with driver.session(database="disease") as session:
            result = session.run("MATCH (d:item) RETURN d.name AS name")
            # Build the result list
            results = []
            for i, record in enumerate(result):
                results.append({'id': i, 'name': record['name']})
            return results

    def find_all_symptom(self):
        driver = self.get_driver()
        with driver.session(database="disease") as session:
            result = session.run("MATCH (d:symptom) RETURN d.name AS name")
            # Build the result list
            results = []
            for i, record in enumerate(result):
                results.append({'id': i, 'name': record['name']})
            return results

    def find_all_symptom_list(self):
        driver = self.get_driver()
        with driver.session(database="disease") as session:
            result = session.run("MATCH (d:symptom) RETURN d.name AS name")
            # Build the result list
            results = []
            for i, record in enumerate(result):
                results.append(record['name'])
            return results

    def find_all_chinese_symptom(self):
        driver = self.get_driver()
        with driver.session(database="disease") as session:
            result = session.run("MATCH (d:symptom) RETURN d.chinese_name AS chinese_name")
            # Build the result list
            results = []
            for i, record in enumerate(result):
                results.append({'id': i, 'chinese_name': record['chinese_name']})
            return results

    def find_all_has_branch(self):
        driver = self.get_driver()
        with driver.session(database="disease") as session:
            # Run the query
            result = session.run("MATCH (n)-[r:HAS_BRANCH]->(m) RETURN n.name AS start_node, m.name AS end_node")
            results = []
            for i, record in enumerate(result):
                results.append([record['start_node'], record['end_node']])
            return results

    def find_all_has_branch_combination(self):
        driver = self.get_driver()
        with driver.session(database="disease") as session:
            # Run the query
            result = session.run("MATCH (n)-[r:HAS_BRANCH_COMBINATION]->(m) RETURN n.name AS start_node, m.name AS end_node")
            results = []
            for i, record in enumerate(result):
                results.append([record['start_node'], record['end_node']])
            return results

    def get_node_hierarchy(self, node_name):
        driver = self.get_driver()
        # with driver.session(database="disease") as session:
        #     node = session.execute_read(self._get_node_by_name, node_name)
        node = self.get_node_by_name(node_name)
        # print('I am finding', node_name, 'found?', node['name'])
        if node is not None:
            hierarchy = {"name": node["name"]}
            hierarchy["children"] = self._get_children(node)
            # print('hierarchy', hierarchy)
            return hierarchy
        else:
            return None

    def _get_children(self, node):
        children = []
        # print('I am in')
        with self.get_driver().session(database="disease") as session:
            node_name = node['name']
            # query = "MATCH (parent)-[]->(child) WHERE parent.name = $parent_name RETURN child"
            query = f"MATCH (parent)-[]->(child) WHERE parent.name = '{node_name}' RETURN child"

            # result = session.read_transaction(self._get_children_recursive, query, node["name"])
            result = session.run(query)
            # print('trying finding')




            # print('get_children', result, 'node name', node["name"],'result.peek()',result.peek())
            if result.peek() is not None:
                for record in result:
                    # print('I can enter the loop')
                    child_node = record["child"]
                    child_hierarchy = {"name": child_node["name"]}
                    child_hierarchy["children"] = self._get_children(child_node)
                    children.append(child_hierarchy)
                # print('children', children)
        # for child_hierarchy in children:
        #     print('child_hierarchy', child_hierarchy)
        #     child_hierarchy["children"] = self._get_children(child_node)

        return children

    @staticmethod
    def _get_children_recursive(tx, query, parent_name):
        result = tx.run(query, parent_name=parent_name)
        return result

    def update_node(self, edit_from, edit_to, label):
        if label == "disease" or label == "item":
            if not edit_from and not edit_to:
                return "Both edit_from and edit_to are empty"
            elif not edit_from and edit_to:
                with self.get_driver().session(database="disease") as session:
                    result = session.write_transaction(self._delete_node, edit_to)
                    return result
            elif edit_from and not edit_to:
                with self.get_driver().session(database="disease") as session:
                    result = session.write_transaction(self._add_node, edit_from, label)
                    return result
            elif edit_from and edit_to:
                with self.get_driver().session(database="disease") as session:
                    result = session.write_transaction(self._update_node, edit_from, edit_to)
                    return result
        else:
            return "Invalid label"

    @staticmethod
    def _delete_node(tx, name):
        query = "MATCH (n) WHERE n.name = $name DELETE n"
        tx.run(query, name=name)

    @staticmethod
    def _add_node(tx, name, label):
        query = "CREATE (n {name: $name, label: $label})"
        tx.run(query, name=name, label=label)

    @staticmethod
    def _update_node(tx, edit_from, edit_to):
        query = "MATCH (n) WHERE n.name = $edit_from SET n.name = $edit_to"
        tx.run(query, edit_from=edit_from, edit_to=edit_to)

    # def _get_children(self, node):
    #     children = []
    #     query = "MATCH (parent)-[]->(child) WHERE ID(parent) = $parent_id RETURN child"
    #     with self.get_driver().session(database="disease") as session:
    #         result = session.read_transaction(self._get_children_recursive, query, node.id)
    #         for record in result:
    #             child_node = record["child"]
    #             child_hierarchy = {"name": child_node["name"]}
    #             child_hierarchy["children"] = self._get_children(child_node)
    #             children.append(child_hierarchy)
    #     return children
    #
    # @staticmethod
    # def _get_children_recursive(tx, query, parent_id):
    #     result = tx.run(query, parent_id=parent_id)
    #     return result

    # def _get_children(self, node):
    #     children = []
    #     query = "MATCH (parent)-[]->(child) WHERE parent.name = $parent_name RETURN child"
    #     with self.get_driver().session(database="disease") as session:
    #         result = session.read_transaction(self._get_children_recursive, query, node["name"])
    #         for record in result:
    #             child_node = record["child"]
    #             child_hierarchy = {"name": child_node["name"]}
    #             child_hierarchy["children"] = self._get_children(child_node)
    #             children.append(child_hierarchy)
    #     return children
    #
    # @staticmethod
    # def _get_children_recursive(tx, query, parent_name):
    #     result = tx.run(query, parent_name=parent_name)
    #     return result


    # local = threading.local()
    #
    #
    # class DB:
    #     def __init__(self):
    #         self.driver = self.get_driver()
    #
    #     def get_driver(self):
    #         # 获取当前线程的数据库连接
    #         if not hasattr(local, 'driver'):
    #             uri = "neo4j+s://06bef84e.databases.neo4j.io"
    #             password = "guw5huMp62eVSJMojt3HC2XLwdQ2oTlItmEmLDsmBx8"
    #             user = "neo4j"
    #             local.driver = GraphDatabase.driver(uri, auth=(user, password))
    #         return local.driver
    #
    #     def close(self):
    #         # 关闭当前线程的数据库连接
    #         driver = getattr(local, 'driver', None)
    #         if driver is not None:
    #             driver.close()
    #             local.driver = None
    # def create_friendship(self, person1_name, person2_name):
    #     with self.driver.session(database="neo4j") as session:
    #         # Write transactions allow the driver to handle retries and transient errors
    #         result = session.execute_write(
    #             self._create_and_return_friendship, person1_name, person2_name)
    #         for row in result:
    #             print("Created friendship between: {p1}, {p2}".format(p1=row['p1'], p2=row['p2']))

    # @staticmethod
    # def _create_and_return_friendship(tx, person1_name, person2_name):
    #     # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
    #     # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
    #     query = (
    #         "CREATE (p1:Person { name: $person1_name }) "
    #         "CREATE (p2:Person { name: $person2_name }) "
    #         "CREATE (p1)-[:KNOWS]->(p2) "
    #         "RETURN p1, p2"
    #     )
    #     result = tx.run(query, person1_name=person1_name, person2_name=person2_name)
    #     try:
    #         return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
    #                 for row in result]
    #     # Capture any errors along with the query and data for traceability
    #     except ServiceUnavailable as exception:
    #         logging.error("{query} raised an error: \n {exception}".format(
    #             query=query, exception=exception))
    #         raise
    #
    # def find_person(self, person_name):
    #     with self.driver.session(database="neo4j") as session:
    #         result = session.execute_read(self._find_and_return_person, person_name)
    #         for row in result:
    #             print("Found person: {row}".format(row=row))
    #
    # @staticmethod
    # def _find_and_return_person(tx, person_name):
    #     query = (
    #         "MATCH (p:Disease) "
    #         "WHERE p.name = $person_name "
    #         "RETURN p.name AS name"
    #     )
    #     result = tx.run(query, person_name=person_name)
    #     return [row["name"] for row in result]


