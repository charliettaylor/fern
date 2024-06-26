/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";
import { BuildingExecutorResponse } from "./BuildingExecutorResponse";
import { RunningResponse } from "./RunningResponse";
import { ErroredResponse } from "./ErroredResponse";
import { StoppedResponse } from "./StoppedResponse";
import { GradedResponse } from "./GradedResponse";
import { GradedResponseV2 } from "./GradedResponseV2";
import { WorkspaceRanResponse } from "./WorkspaceRanResponse";
import { RecordingResponseNotification } from "./RecordingResponseNotification";
import { RecordedResponseNotification } from "./RecordedResponseNotification";
import { InvalidRequestResponse } from "./InvalidRequestResponse";
import { FinishedResponse } from "./FinishedResponse";

export const CodeExecutionUpdate: core.serialization.Schema<
    serializers.CodeExecutionUpdate.Raw,
    SeedTrace.CodeExecutionUpdate
> = core.serialization
    .union("type", {
        buildingExecutor: BuildingExecutorResponse,
        running: RunningResponse,
        errored: ErroredResponse,
        stopped: StoppedResponse,
        graded: GradedResponse,
        gradedV2: GradedResponseV2,
        workspaceRan: WorkspaceRanResponse,
        recording: RecordingResponseNotification,
        recorded: RecordedResponseNotification,
        invalidRequest: InvalidRequestResponse,
        finished: FinishedResponse,
    })
    .transform<SeedTrace.CodeExecutionUpdate>({
        transform: (value) => {
            switch (value.type) {
                case "buildingExecutor":
                    return SeedTrace.CodeExecutionUpdate.buildingExecutor(value);
                case "running":
                    return SeedTrace.CodeExecutionUpdate.running(value);
                case "errored":
                    return SeedTrace.CodeExecutionUpdate.errored(value);
                case "stopped":
                    return SeedTrace.CodeExecutionUpdate.stopped(value);
                case "graded":
                    return SeedTrace.CodeExecutionUpdate.graded(value);
                case "gradedV2":
                    return SeedTrace.CodeExecutionUpdate.gradedV2(value);
                case "workspaceRan":
                    return SeedTrace.CodeExecutionUpdate.workspaceRan(value);
                case "recording":
                    return SeedTrace.CodeExecutionUpdate.recording(value);
                case "recorded":
                    return SeedTrace.CodeExecutionUpdate.recorded(value);
                case "invalidRequest":
                    return SeedTrace.CodeExecutionUpdate.invalidRequest(value);
                case "finished":
                    return SeedTrace.CodeExecutionUpdate.finished(value);
                default:
                    return SeedTrace.CodeExecutionUpdate._unknown(value);
            }
        },
        untransform: ({ _visit, ...value }) => value as any,
    });

export declare namespace CodeExecutionUpdate {
    type Raw =
        | CodeExecutionUpdate.BuildingExecutor
        | CodeExecutionUpdate.Running
        | CodeExecutionUpdate.Errored
        | CodeExecutionUpdate.Stopped
        | CodeExecutionUpdate.Graded
        | CodeExecutionUpdate.GradedV2
        | CodeExecutionUpdate.WorkspaceRan
        | CodeExecutionUpdate.Recording
        | CodeExecutionUpdate.Recorded
        | CodeExecutionUpdate.InvalidRequest
        | CodeExecutionUpdate.Finished;

    interface BuildingExecutor extends BuildingExecutorResponse.Raw {
        type: "buildingExecutor";
    }

    interface Running extends RunningResponse.Raw {
        type: "running";
    }

    interface Errored extends ErroredResponse.Raw {
        type: "errored";
    }

    interface Stopped extends StoppedResponse.Raw {
        type: "stopped";
    }

    interface Graded extends GradedResponse.Raw {
        type: "graded";
    }

    interface GradedV2 extends GradedResponseV2.Raw {
        type: "gradedV2";
    }

    interface WorkspaceRan extends WorkspaceRanResponse.Raw {
        type: "workspaceRan";
    }

    interface Recording extends RecordingResponseNotification.Raw {
        type: "recording";
    }

    interface Recorded extends RecordedResponseNotification.Raw {
        type: "recorded";
    }

    interface InvalidRequest extends InvalidRequestResponse.Raw {
        type: "invalidRequest";
    }

    interface Finished extends FinishedResponse.Raw {
        type: "finished";
    }
}
