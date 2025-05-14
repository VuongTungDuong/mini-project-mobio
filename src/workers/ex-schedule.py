from datetime import datetime
from typing import TypedDict

from mobio.libs.m_scheduler_partitioning.m_scheduler import MobioScheduler
from mobio.libs.m_scheduler_partitioning.scheduler_models.scheduler_state_model import (
    SchedulerStateModel,
)
from pymongo import UpdateOne
from src.models.email_model import EMAIL, EmailStatus
from src.modules.db import db


class EmailScheduler(TypedDict):
    _id: str
    partition: int
    status: str
    email: str
    created_at: datetime


class SendEmailScheduler(MobioScheduler):
    def process(self):
        if self.url_connection:
            SchedulerStateModel(self.url_connection).set_busy(worker_id=self.node_id)
        print("Partitions assigned to this worker: ", self.lst_partitions)

        # kiem tra xem phai xu ly bao nhieu partition hay khong
        # lay so luong theo tung partition toi da 5 don vi xa nhat
        # chuyen trang thai tu checking sang processing
        # neu khong phai xu ly thi chuyen trang thai tu processing sang done
        if len(self.lst_partitions) != 0:
            # xu ly cac partition hoac xu ly het cac partition
            for partition in self.lst_partitions:
                # lay so luong email toi da 5 don vi
                # neu khong phai xu ly thi chuyen trang thai tu processing sang done

                # lay ra ca
                data: list[EmailScheduler] = (
                    db[EMAIL.TABLE]
                    .find({"partition": partition, "status": EmailStatus.CHECKING})
                    .limit(5)
                    .sort({"creaded_at": 1})
                    .to_list()
                )

                # #  chuyen trang thai tu checking sang processing
                updates: list[UpdateOne] = []
                for item in data:
                    updates.append(
                        UpdateOne(
                            {"_id": item["_id"]},
                            {
                                "$set": {
                                    "status": EmailStatus.PROCESSING,
                                }
                            },
                        )
                    )

                if len(updates) == 0:
                    print(f"No emails to process in partition {partition}")
                    continue

                status = db[EMAIL.TABLE].bulk_write(updates)
                if status.modified_count != len(updates):
                    raise Exception(
                        f"Failed to update status for partition {partition}"
                    )
                # exit(0)


if __name__ == "__main__":
    SendEmailScheduler(
        root_node="kafka2",
        nop=10,
        delays=10,
        url_connection="mongodb://root:root123@localhost:27017/email_db?authSource=admin",
        zookeeper_uri="0.0.0.0:2181",
    )
