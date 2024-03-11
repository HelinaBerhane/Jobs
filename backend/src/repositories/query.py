from typing import any


def format_where_in_list(values: list[Any]) -> str:
    return {"(" + ",".join(":"+str(i) for i in range(len(values))) + ")"}

# class QueryCondition:
#     def __init__(self) -> None:
#         raise NotImplementedError

#     def dump(self) -> str:
#         raise NotImplementedError

# class QueryWhereEquals(QueryCondition):
#     def __init__(
#         self,
#         matching_column: str,
#         matching_value: Any,
#     ) -> None:
#         # TODO: aware the signature not matching parent's isn't ideal, fix later
#         self.matching_column = matching_column
#         self.matching_value = matching_value

#     def dump(self) -> str:
#         return "f{self.matching_column} = (?)"

# class QueryWhereInList(QueryCondition):
#     def __init__(
#         self,
#         matching_column: str,
#         matching_values: list[Any],
#     ) -> None:
#         # TODO: aware the signature not matching parent's isn't ideal, fix later
#         self.matching_column = matching_column
#         self.matching_values = matching_values

#     def dump(self) -> str:
#         # return "(" + ",".join(":"+str(i) for i in range(len(self.matching_values))) + ")"
#         return "(" + ",".join("?" for _ in range(len(self.matching_values))) + ")"

# class QueryConditions:
#     # TODO: move this to a separate folder
#     # TODO: write tests for these
#     def __init__(
#         self,
#         conditions: tuple[QueryCondition]
#     ) -> None:
#         self.conditions = conditions

#     def dump(self) -> str:
#         return ",".join(c.dump() for c in self.conditions)

# def select_query(
#     table: str,
#     columns: tuple[str],
#     conditions: QueryConditions | None = None,
# ) -> str:
#     return f"SELECT {columns} FROM {table} {'WHERE ' + conditions.dump()};"

# select_query(
#     table="jobs",
#     columns=(
#         id,
#         name,
#         datetime(created_date,'utc') as created_date,
#     ),
#     conditions=

# )

#             SELECT
#             FROM
#                 jobs
#             """
#         if job_ids:
#             query += f"""
#                 WHERE
#                     id
#                 IN

#                 """
#     """
